from github import Github
from .email_checker import EmailChecker
from .celeryutils import countdown
import sqlite3
from datetime import datetime
import sys
import time
from urllib.parse import urlparse

class GithubConnector:
    def __init__(self, github_token):
        self.github = Github(github_token)
        try:
            self.db_conn = sqlite3.connect("/home/celery/db.sqlite3")
        except Exception as e:
            print(e)
            self.db_conn = sqlite3.connect("db.sqlite3")
        self.db_cursor = self.db_conn.cursor()
        # create table
        sqlite_create_table = "CREATE TABLE IF NOT EXISTS github_responses(contributor_id TEXT, email TEXT, location TEXT, request_date DATETIME)"
        self.sqlite_insert_with_param = """INSERT INTO 'github_responses'
                          ('contributor_id', 'email', 'location','request_date') 
                          VALUES (?, ?, ?, ?);"""
        self.db_cursor.execute(sqlite_create_table)
        self.db_conn.commit()
        self.db_cursor.close()

    def getContributorInfo(self, id):
        try:
            repo = self.github.get_repo(int(id))
        except:
            return []
        contributors = repo.get_contributors()
        emails_list = []
        for contributor in contributors:
            requests_remaining=self.github.rate_limiting
            if requests_remaining[0] < 100:
                wait_time=self.github.rate_limiting_resettime - int(time.time())
                print("No Github requests remaining")
                countdown(wait_time)
            self.db_cursor = self.db_conn.cursor()
            contr_id = contributor.id
            location = contributor.location
            sqlite_select_query = """SELECT email from github_responses WHERE contributor_id = ?"""
            self.db_cursor.execute(sqlite_select_query, (contr_id,))
            email = self.db_cursor.fetchall()
            if(not email):
                try:
                    email = contributor.email
                    time_ = datetime.now().strftime("%B %d, %Y %I:%M%p")
                    data_tuple = (contr_id, email, location, time_)
                    self.db_cursor.execute(
                        self.sqlite_insert_with_param, data_tuple)
                    self.db_conn.commit()
                except Exception as e:
                    print(e)
                    email = ""
            else:
                email = email[0][0]

            if EmailChecker.checkMail(email):
                emails_list.append(email)
            else:
                if(email):
                    print("wrong email " + email)
            self.db_cursor.close()
        return emails_list

    def GetProjectID(self, repo_url):
        parser = urlparse(repo_url) 
        owner = parser.path.split('/')[1]
        project_name = parser.path.split('/')[2]
        try:
            project_name = project_name.split('.')[0]
        except:
            pass 
        repo = self.github.get_repo(owner+'/'+project_name)
        return repo.id


if __name__ == "__main__":
    pass

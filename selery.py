#!/usr/bin/python3

from openselery import openselery

def main():
    print("=============================")
    ### instantiate openselery and 
    ### let it initialize configurations,
    ### arguments and environments
    selery = openselery.OpenSelery()
    ### let openselery connect to
    ### various APIs and servers to 
    ### allow data gathering
    selery.connect()
    ### let openselery gather data
    ### of all involved projects, 
    ### dependencies and contributors
    projects, deps, contributors = selery.gather()
    ### let openselery roll the dice 
    ### and choose some lucky contributors
    ### who should receive donations
    recipients = selery.choose(contributors)
    ### let openselery use the given
    ### wallet containing virtual currency
    ### to pay out the selected contributors
    selery.payout(recipients)
    ### Done.
    print("=============================")


if __name__ == "__main__":
    main()

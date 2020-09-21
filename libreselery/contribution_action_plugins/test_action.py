#! /usr/bin/python3

from libreselery.configuration import LibreSeleryConfig
from libreselery.contribution_distribution_engine_types import (
    Contributor,
    ContributionAction,
    ContributionActionPlugin,
)

### Start User Imports
### specialzed plugin imports can be added here
##################################################################################
import sys

### End User Imports
##################################################################################


class MY_TEST_ACTION_PLUGIN_CLASS(ContributionActionPlugin):
    """
    This class is a plugin containing the implementation of a single ContributorAction.
    It is responsible for gathering contributor information and evaluating scores
    for each contributor based on configurated metrics

    Plugin description:
    This plugin does nothing special, it's just for testing and showcasing how
    to use and implement plugins in the action lifecycle of the CDE.
    It will just return a random contributor list and some randome scores.
    """

    _alias_ = "test_action"

    def __init__(self):
        super(MY_TEST_ACTION_PLUGIN_CLASS, self).__init__()

    def initialize_(self, action):
        """
        Overload of abstract method which is responsible for initializing this plugin

        Parameters:
        action (ContributionAction):
            action object which contains all necessary information of what
            a contributor has to doto be scored and recognized as such

        Returns:
        bool: True if successfully initialized
        """
        self.log("INIT")
        return True

    def onGlobalsUpdate_(self):
        """
        Overload of abstract event method which signalizes the change of the global configuration

        Parameters:
        None

        Returns:
        None
        """
        ### example
        self.someGlobalInformation = self.getGlobals().simulation
        pass

    def gather_(self, cachedContributors=[]):
        """
        Overload of abstract method which is responsible for gathering
        contributor information and scoring contributors based on the action defined

        Parameters:
        [optional] cachedContributors (list):
            list of contributors from various external (remote) sources which had been chached earlier
            so that plugins don't need to do expensive lookups all the time

        Returns:
        tuple: (list of contributors, list of scores)
        """
        self.log("GATHER > This is a simulation: %s" % self.someGlobalInformation)
        # contributors = [("nickfiege999@gmail.com", "kikass13"), ("randomEmail@random.rand", "otherUser")]
        contributors = [
            Contributor("kikass13", "nickfiege999@gmail.com"),
            Contributor("Tobias Augspurger", "ly0@protonmail.com"),
        ]
        scores = [1337.0, 50.0]
        self.log(contributors)
        self.log(scores)
        return contributors, scores

    ### Start User Methods
    ### specialzed plugin methods can be added here
    ##################################################################################
    ###
    ### def work(self):
    ###     pass
    ###
    ### Énd User Methods
    ##################################################################################


def test():
    success = False
    print("This is a Test!")
    ### define our input configuration (action) which normally comes from .yml configuration
    d = {
        "test_action_id": {
            "debug": True,
            "type": "test_action",  ### type of action (also the name of the plugin _alias_ used!)
        }
    }
    ### create an action object
    action = ContributionAction(d)
    ### initialize the action
    ### which will in turn use this specific plugin
    ### if configured correctly
    init = action.initialize_()
    ### emulate some global information
    ### which is used by the plugin to work properly
    config = LibreSeleryConfig({"simulation": True})
    action.updateGlobals(config=config, connectors=None)
    ### preparations done, lets do something
    if init:
        ### let us do our work
        contributors, scores = action.gather_()
        ### visualize and finalize gathered data
        print("Result:")
        print("contributors:\n%s" % contributors)
        print("scores:\n%s" % scores)
        ### evaluate test data
        if len(contributors) == len(scores):
            success = True
    ### Done
    return success


if __name__ == "__main__":
    assert test() == True



from project import services
from project import constants
import mock
import unittest
from mock import patch
from mock import Mock


# Third-party imports...
from nose.tools import assert_list_equal, assert_true
from unittest import skipIf



@skipIf(constants.SKIP_REAL, 'Skipping tests that hit the real API server.')
def test_integration_contract():

    ##########################
    #  prints will be surpressed when runs  unless -s  given with nosetests --verbosity=2 project 
    ####################################################################

    # Call the service to hit the actual API.
    actual = services.get_headers()
    print  "==============================================="

    print (actual);   
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
    
    for key in actual:
            print "the key name is " + key + " and its value is " + actual[key]
          
    print ("content-type") 
    content_type = actual.get("Content-Type")
    x_backend_server = actual.get("X-Backend-Server")
    print content_type  
    print x_backend_server
    print "================================================="

     

    assert_true (content_type == constants.content_type)
    #assert_true (x_ackend_server == constants.web2)
 

Feature: Simple VLAN management
  As a Network Controller,
  I want to deploy and remove VLANs on network elements.

  Scenario: Plain VLAN 100
    Given the network mentioned in network.csv
    When the controller deploys VLAN 100
    Then the traffic should pass on this VLAN
     And this VLAN should be in the configuration

  Scenario: Plain VLAN 100 Removal
    Given the network mentioned in network.csv
    When the controller removes VLAN 100
    Then the traffic should not pass on this VLAN
     And this VLAN should not be in the configuration

  Scenario Outline: Deploy VLAN independanly
    Given the network mentioned in network.csv
    # When the VLAN <vlan_id> is deployed
    When the controller deploys VLAN <vlan_id>
    Then the traffic should pass on this VLAN
     And this VLAN should be in the configuration

    Examples:
      | vlan_id |
      |     100 |
      |     200 |
  
  Scenario: Multiple VLANs
    Given the network mentioned in network.csv
    #  And the VLANs 300 to 400 by step of 2
    # When all these VLANs are deployed
    When the controller deploys VLANs 300 to 400 by step of 50
    Then the traffic should pass on all these VLANs

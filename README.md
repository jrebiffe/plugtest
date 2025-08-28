# ETSI 5th mWT Plugtest

Automated Testsuite for ETSI 5th mWT Plugtest using Robot Framework Gherkin Parser.

## Installation instructions

```sh
pip install robotframework-gherkin-parser
```

## Execute the test suite

```sh
robot --parser GherkinParser features/
```
Robot

## Explainations

The file `features/vlan.feature` follows the
[Gherkin language](https://cucumber.io/docs/gherkin/reference).
It reads like plain English sentences and each `Scenario` is a single test.
The test suite currently contains only 5 tests and does not actually connects
to network elements via NETCONF.

The list of network elements are in `network.csv`.

```mermaid
graph TD;
    vlan.feature --> vlan_keywords.resource
    vlan_keywords.resource --> NetconfLibrary.py
    vlan_keywords.resource --> TesterLibrary.py
    NetconfLibrary.py --> Network_Elements_via_NETCONF
    TesterLibrary.py --> Asks_user_for_manual_check

    class vlan.feature feature
    class network.csv,vlan_keywords.resource resource
    class NetconfLibrary.py,TesterLibrary.py feature
    class Network_Elements_via_NETCONF,Asks_user_for_manual_check action

    classDef feature color:yellow
    classDef resource color:red
    classDef python color:blue
    classDef action color:green
```

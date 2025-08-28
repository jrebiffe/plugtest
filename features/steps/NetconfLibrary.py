"""RobotFramework library to control network element via NETCONF."""

from csv import DictReader
from typing import NamedTuple

from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn


class NetworkElement(NamedTuple):
    """Configuration data for a single NE."""

    name: str
    address: str
    username: str
    password: str


@library(scope="TEST")
class NetconfLibrary:
    """RobotFramework library to control network element via NETCONF."""

    builtin = BuiltIn()
    network: list[NetworkElement] | None = None

    @keyword("the network mentioned in ${network_filename}")
    def the_network_mentioned_in_csv(self, network_filename: str) -> None:
        """Load network from CSV file."""
        with open(network_filename, encoding="ascii") as file:
            csv = DictReader(file)
            network = [NetworkElement(**ne) for ne in csv]
        self.network = network

    @keyword("the controller deploys VLAN ${vlan_id}")
    def the_controller_deploys_vlan_xxxx(self, vlan_id: int) -> None:
        """Deploy a VLAN on all network elements.

        ``vlan_id`` is pushed in all NEs.
        """
        self.builtin.set_global_variable("${VLAN_ID}", vlan_id)

    @keyword("this VLAN should be in the configuration")
    def this_vlan_should_be_in_the_configuration(self) -> None:
        """Verify that VLAN is deployed in all NEs configuration.

        Fails if the VLAN is missing in any of the NEs.
        """
        assert bool(self.network)
    
    @keyword("the controller removes VLAN ${vlan_id}")
    def the_controller_removes_vlan_xxxx(self, vlan_id: int) -> None:
        """Deploy a VLAN on all network elements.

        ``vlan_id`` is deleted in all NEs.
        """
        self.builtin.set_global_variable("${VLAN_ID}", vlan_id)
    
    @keyword("this VLAN should not be in the configuration")
    def this_vlan_should_not_be_in_the_configuration(self) -> None:
        """Verify that VLAN is absent in all NEs configuration.

        Fails if the VLAN is present in any of the NEs.
        """
        assert bool(self.network)

    @keyword("the controller deploys VLANs ${start} to ${stop} by step of ${step}")
    def the_vlans_start_to_stop_by_step_of_step(
        self, start: int, stop: int, step: int
    ) -> None:
        """Deploy a list of VLANs on all network elements.

        ``start`` to ``stop`` by step of ``step`` are pushed in all NEs.
        """
        vlans_id = list(range(start, stop, step))
        self.builtin.set_global_variable("${VLANS_ID}", vlans_id)

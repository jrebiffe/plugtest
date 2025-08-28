"""RobotFramework library to control Manual verification of tester."""

from robot.api import Error
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Dialogs import execute_manual_step


@library(scope="TEST")
class TesterLibrary:
    """RobotFramework library to control Manual verification of tester."""

    builtin = BuiltIn()

    @keyword
    def the_traffic_should_pass_on_this_vlan(self) -> None:
        """Fails if the traffic don't pass on the VLAN."""
        vlan_id = self.builtin.get_variable_value(r"\${VLAN_ID}")
        if vlan_id is None:
            raise Error("Variable VLAN_ID does not exist.")

        execute_manual_step(
            "Verify if the traffic pass accross network elements, "
            f"on VLAN {vlan_id}.\n\n Did the traffic passed?",
            f"Traffic does not pass on VLAN {vlan_id}.")
        # -if choice((True, False)):
        #    raise Failure(f"Traffic does not pass on VLAN {vlan_id}.")
    
    @keyword
    def the_traffic_should_not_pass_on_this_vlan(self) -> None:
        """Fails if the traffic pass on the VLAN."""
        vlan_id = self.builtin.get_variable_value(r"\${VLAN_ID}")
        if vlan_id is None:
            raise Error("Variable VLAN_ID does not exist.")

        execute_manual_step(
            "Verify if the traffic is blocked accross network elements, "
            f"on VLAN {vlan_id}.\n\n Is the traffic blocked?",
            f"Traffic does not pass on VLAN {vlan_id}.")

    @keyword
    def the_traffic_should_pass_on_all_these_vlans(self) -> None:
        """Fails if the traffic don't pass on several VLANs."""
        vlans_id = self.builtin.get_variable_value(r"\${VLANS_ID}")
        if vlans_id is None:
            raise Error("Variable VLANS_ID does not exist.")

        execute_manual_step(
            "Verify if the traffic pass accross network elements, "
            f"on VLAN {vlans_id}.\n\n Did the traffic passed?",
            f"Traffic does not pass on VLAN {vlans_id}.")

def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

def should_message_disappear(self):
    assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message did not disappear"




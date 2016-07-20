from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    def get_company(self):
        return self.context.getProperty('company', '')

    def set_company(self, value):
        return self.context.setMemberProperties({'company': value})

    company = property(get_company, set_company)

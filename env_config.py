class EnvConfig:
    DEV_URL = "https://dev.workflowpro.com"
    STAGING_URL = "https://staging.workflowpro.com"
    PROD_URL = "https://app.workflowpro.com"

    @staticmethod
    def get_url(env_name):
        if env_name == "dev":
            return EnvConfig.DEV_URL
        elif env_name == "staging":
            return EnvConfig.STAGING_URL
        return EnvConfig.PROD_URL

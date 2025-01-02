from globalog import LOG

# It will automatically load configuration
LOG.info("This works without explicit initialization")

# Or explicitly initialize with custom config
# LOG.init(config_file="my_config.json")
def get_kedro_component_versions():
    from importlib.metadata import version

    version_msg_list = [
        f"The following components are installed with kedro-pack ({version('kedro_pack')}):",
        f" - kedro: {version('kedro')}",
        f" - kedro-datasets: {version('kedro_datasets')}",
        f" - kedro-airflow: {version('kedro_airflow')}",
        f" - kedro-mlflow: {version('kedro_mlflow')}",
        f" - kedro-viz: {version('kedro_viz')}",
        f" - kedro-light: {version('kedro_light')}",
    ]

    print("\n".join(version_msg_list))

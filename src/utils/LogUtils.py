from pathlib import Path

from loguru import logger


def logging_config(log_rotation, log_retentionm, log_path=None, log_name="agiled"):
    """
    设置日志信息, 使用模块为 loguru
    :param log_rotation:
    :param log_retentionm:
    :param log_path:
    :return:
    """
    log_path = log_path if log_path else Path.cwd().joinpath("logs").joinpath(log_name+".log")
    logger.add(
        log_path,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        enqueue=True,
        backtrace=False,
        rotation=log_rotation,
        retention=log_retentionm,
        compression="zip",
    )

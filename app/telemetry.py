
from datadog import initialize, statsd
import logging, json

initialize(statsd_host="localhost", statsd_port=8125)

logger = logging.getLogger("ai-sre-copilot")
logger.setLevel(logging.INFO)

def emit_metrics(latency, tokens, error_rate, hallucination, cost):
    statsd.gauge("llm.response.latency_ms", latency)
    statsd.gauge("llm.tokens.total", tokens)
    statsd.gauge("llm.error.rate", error_rate)
    statsd.gauge("llm.hallucination.score", hallucination)
    statsd.gauge("llm.cost.estimated_usd", cost)

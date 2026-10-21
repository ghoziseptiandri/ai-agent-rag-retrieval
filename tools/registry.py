from tools.calculator import calculate
from tools.time_tool import get_current_time
from long_term_memory import save_memory, update_memory, delete_memory
from tools.file_reader import read_file
from tools.weather import get_weather
from tools.rag import search_knowledge_base

TOOL_FUNCTIONS = {
    "calculate": calculate,
    "get_current_time": get_current_time,
    "save_memory": save_memory,
    "update_memory": update_memory,
    "delete_memory": delete_memory,
    "read_file": read_file,
    "get_weather": get_weather,
    "search_knowledge_base": search_knowledge_base,
}
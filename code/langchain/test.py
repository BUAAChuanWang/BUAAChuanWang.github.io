import os

# Michael
os.environ["OPENAI_API_KEY"] = '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'


# from langchain.llms import OpenAI
#
# llm = OpenAI(model_name="gpt-3.5-turbo", max_tokens=1024)
# llm("怎么评价人工智能")

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

# 加载 OpenAI 模型
llm = OpenAI(temperature=0, max_tokens=2048)

 # 加载 serpapi 工具
tools = load_tools(["serpapi"])
# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run("What's the date today? What great events have taken place today in history?")
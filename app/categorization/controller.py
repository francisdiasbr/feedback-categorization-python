from flask import request, jsonify

from langchain_community.callbacks import get_openai_callback

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.pydantic_v1 import BaseModel, Field

from langchain_openai import ChatOpenAI

from typing import List

import os


class Comment(BaseModel):
  """Comment Schema"""

  id: int = Field(description="ID do comentário")

  comment: str = Field(description="Comentário")
  
  category: str = Field(description="Categorização")


class GradeSchema(BaseModel):
  """Grade Schema"""

  comments: List[Comment] = Field(description="Lista com os comentários categorizados")


def llm_decorator(func, obj):
  
  with get_openai_callback() as cb:
    
    invoked = func.invoke(obj)

    print('\ncallback\n', cb, '\n')

  return invoked


def comment_categorization(api_key, categories, comments, instructions, model):

  print('\nstart chat completion')

  llm = ChatOpenAI(api_key=api_key, model=model)

  data_object = {
    "categories": categories,
    "instructions": instructions,
    "question": {
      "comments": comments
    },
  }

  result = []

  try:
    
    conversation = []
    
    human_message = "Comments: {question}"

    system_message = """Instructions: {instructions} \n\n Categories: {categories}"""

    conversation.append(("human", human_message))
    
    conversation.append(("system", system_message))

    route_prompt = ChatPromptTemplate.from_messages(conversation)

    llm_router = llm.with_structured_output(schema=GradeSchema)
    
    llm_chain = route_prompt | llm_router

    response = llm_decorator(llm_chain, data_object)

    for comment in response.comments:
      result.append(comment.dict())

  except Exception as error:
    print(f"\nException: {error}\n")
    return jsonify({"ok": False, "data": error.message}), 500

  return jsonify({"ok": True, "data": result}), 200
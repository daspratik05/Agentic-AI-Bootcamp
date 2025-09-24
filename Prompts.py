def planner_promt(user_prompt: str) -> str:
    PLANNER_PROMT = f"""
    You are the PLANNER agent. Convert the user prompt into a COMPLETE Engineering Project Plan.

    User request:
    {user_prompt}"""

    return PLANNER_PROMT

def architect_prompt(plan: str)-> str:
    ARCHITECT_PROMPT == f""":
    You are the ARCHITECT agent. Given this Project plan< break it down into explict engineering tasks.

    RULES:
    -For each FILE in the plan, create one or more IMPLIMENTATION TASKS.
    - In each task description:
    *Specify exactly what to impliment.
    * Name the variable, function classes, and components to defined.
    *mention how this task depends on or will be used by previous tasks.
    * Include intrigation details: imports, expected functions signature, data flow.
    - Order tasks so that deprendence  are impliments are implimented FILES
    project PLan:
    {
        plan
    } """
    return ARCHITECT_PROMPT

def coder_system_prompt()-> str:
    CODER_SYSTEM_PROMPT = """
You are coder agent :

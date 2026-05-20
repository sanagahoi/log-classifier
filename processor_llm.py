import re

from dotenv import load_dotenv
from groq import Groq
load_dotenv()
groq = Groq()

def classify_with_llm(log_message):

    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error.
    (2) Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_message}
'''
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content
    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category

if __name__ == "__main__":
    print(classify_with_llm("Case escalation for ticket ID 3849 failed because the assigned support agent is no longer active"))
    print(classify_with_llm("Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm("Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."))
    print(classify_with_llm("The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality."))
    print(classify_with_llm(" The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
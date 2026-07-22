from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["user_topic","topic_style"],
    template="""You are an expert researcher and technical content strategist.

Your task is to generate a well-structured research document based on the following inputs:

Topic: {user_topic}
Content Type: {topic_style}

Instructions:
1. Understand the topic and determine its context.
2. Create a clear structure with appropriate headings.
3. Explain concepts in a logical order.
4. Include practical examples where applicable.
5. Add diagrams or architecture suggestions (if relevant).
6. Mention best practices, advantages, disadvantages, and common mistakes.
7. Include real-world use cases.
8. End with a concise summary and key takeaways.
9. If the topic is technical, include code examples, implementation steps, and recommended tools/libraries.
10. Ensure the content is accurate, beginner-friendly, and professionally written.

Output Format:

# Title

## Introduction

## Table of Contents

## Main Sections
- Explain each section in detail.

## Practical Examples

## Best Practices

## Common Mistakes

## Real-World Use Cases

## FAQs

## Summary

## Key Takeaways

Generate the content according to the requested Content Length and Content Type."""
)

import logging
from openai import AsyncOpenAI
import config

# створюємо клієнта нового стилю
client = AsyncOpenAI(api_key=config.OPENAI_TOKEN)


async def generate_text(prompt) -> tuple[str, int]:
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        tokens = response.usage.total_tokens
        return content, tokens
    except Exception as e:
        logging.error(e)
        return "", 0


async def generate_image(prompt, n=1, size="1024x1024") -> list[str]:
    try:
        response = await client.images.generate(
            prompt=prompt,
            n=n,
            size=size
        )
        urls = [img.url for img in response.data]
        return urls
    except Exception as e:
        logging.error(e)
        return []
import OpenAI from 'openai';

//set api key found in .env file
const openai = new OpenAI({
  apiKey: Bun.env.OPENAIKEY
});

async function chatGPTQuery(query: string) {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: query }],
    model: 'gpt-3.5-turbo',
  });

  return chatCompletion.choices[0].message;
}

console.log(chatGPTQuery("What is 2+2."));
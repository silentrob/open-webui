import { getRAGTemplate } from '$lib/apis/rag';

export const PersonaTemplate = async (token: string, context: string, query: string) => {
	let template = await getRAGTemplate(token).catch(() => {
		return `Given following personality traits, synthesize them down into a character card that best describes your personality. 
      Each trait is between 1 ~ 10

      Your Emotional Traits {{emotional}}
      Your Social Traits {{social}}
      Your Behavioural Traits {{behavioral}}
      Your Cognitive Traits {{cognitive}}
      Your Physical Heath Traits {{physical_health}}
      Your Moral Traits {{moral}}
      Your Communication Traits {{communication}}`;

    });

	// template = template.replace(/\[context\]/g, context);
	// template = template.replace(/\[query\]/g, query);

	return template;
};

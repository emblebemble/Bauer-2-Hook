from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
# import boto3  # Uncomment for AWS Polly TTS integration

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure API keys
openai.api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'your-aws-key-here')  # Uncomment for AWS Polly
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'your-aws-secret-here')  # Uncomment for AWS Polly

def generate_podcast_intros(theme):
    """
    Generate three podcast intro variants and psychological analysis using OpenAI's API
    with advanced psychological techniques and diverse hooks
    """
    prompt = f"""Generate three unique 15-20 sec intros for a {theme} podcast using advanced 
    psychological techniques. 

    REQUIREMENTS FOR VARIANTS:

    1) Psychological Hook Rotation (use a different technique for each variant):
       - Curiosity Gap Theory (Loewenstein): Create knowledge gaps through unexpected questions
       - Narrative Transportation: Use incomplete story arcs to drive engagement
       - Social Proof + Authority: Leverage collective experience or expert validation
       - Mystery + Anticipation: Employ implied knowledge gaps with future payoff
    
    2) LIWC-Based Language Selection:
       - Cognitive Process Words: Use insight, causation, and discrepancy terms
       - Emotional Process Words: Balance affect terms based on Pennebaker's research
       - Social Process Words: Include relationship and group dynamic terms
       - Power and Achievement Words: Incorporate status and accomplishment markers
    
    3) Psychological Urgency Triggers:
       - Scarcity Principle: Time or access limitations
       - Exclusivity Effect: Insider or privileged access framing
       - Temporal Immediacy: Present-moment engagement hooks
       - Social Momentum: Group movement and collective action frames
    
    4) Technical Requirements:
       - NO clichéd phrases or overused hooks
       - Each variant must employ distinct psychological techniques
       - Include [Podcast Name] as a placeholder
       - Maintain Bauer Audio's bold, authoritative style
       - Mix statement and question hooks for variety

    REQUIRED ANALYSIS STRUCTURE:

    1. LIWC Framework Analysis
       1.1 Word Category Breakdown
           - List and analyze cognitive process words
           - List and analyze emotional process words
           - List and analyze social process words
       1.2 Linguistic Style Markers
           - Authenticity indicators
           - Cognitive complexity metrics
           - Temporal orientation patterns

    2. Pennebaker Psychological Framework
       2.1 Emotional Expression Analysis
           - Emotional tone evaluation
           - Disclosure pattern assessment
           - Authenticity markers
       2.2 Cognitive Processing Indicators
           - Analytical thinking patterns
           - Cognitive complexity markers
           - Insight and causation signals

    3. Variant-Specific Technique Analysis
       3.1 Variant 1 Breakdown
           - Primary psychological principles used
           - Expected cognitive impact
           - Behavioral activation potential
       3.2 Variant 2 Breakdown
           - Primary psychological principles used
           - Expected cognitive impact
           - Behavioral activation potential
       3.3 Variant 3 Breakdown
           - Primary psychological principles used
           - Expected cognitive impact
           - Behavioral activation potential

    4. Engagement Metrics Prediction
       4.1 Quantitative Predictions
           - Expected engagement rate
           - Retention probability
           - Call-to-action response rate
       4.2 Qualitative Impact
           - Emotional resonance prediction
           - Social sharing potential
           - Community building impact

    Format each variant on a new line, followed by the structured analysis using the exact headers and subheaders above."""

    try:
        # If no API key is provided, return mock responses
        if not openai.api_key or openai.api_key == 'your-api-key-here':
            mock_responses = {
                'true crime': {
                    'variants': [
                        'Behind the evidence lies a riddle. [Podcast Name] unravels shocking testimonies—insider access opens.',
                        'Listeners are uncovering buried confessions. [Podcast Name] delivers exclusive breakthroughs—your rare glimpse awaits.',
                        'The untold chapter begins... [Podcast Name] exposes hidden motives—join the investigation movement.'
                    ],
                    'analysis': """1. LIWC Framework Analysis
    1.1 Word Category Breakdown
        • Cognitive Process Words:
          - Insight: "unravels" (98th percentile), "exposes" (95th percentile)
          - Causation: "lies" (85th percentile)
          - Discrepancy: "hidden" (92nd percentile)
        • Emotional Process Words:
          - Negative: "shocking" (88th percentile), "buried" (75th percentile)
          - Tension: "riddle" (82nd percentile)
        • Social Process Words:
          - Group References: "listeners" (90th percentile)
          - Testimony Words: "confessions" (95th percentile)

    1.2 Linguistic Style Markers
        • Authenticity Indicators: 89th percentile (high revelatory language)
        • Cognitive Complexity: 92nd percentile
        • Temporal Focus: Present-dominant with future implications

2. Pennebaker Psychological Framework
    2.1 Emotional Expression Analysis
        • Emotional Tone: Moderate tension (7.2/10) with mystery elements
        • Disclosure Pattern: Progressive revelation structure
        • Authenticity Markers: High personal truth-seeking language

    2.2 Cognitive Processing Indicators
        • Analytical Thinking: 85th percentile
        • Complexity Markers: Multi-layered mystery framing
        • Insight Signals: Strong causal relationship patterns

3. Variant-Specific Technique Analysis
    3.1 Variant 1 Breakdown
        • Principles: Loewenstein's Information Gap + Mystery
        • Cognitive Impact: Creates immediate curiosity tension
        • Activation: High investigative drive (8.5/10)

    3.2 Variant 2 Breakdown
        • Principles: Social Proof + Scarcity
        • Cognitive Impact: Triggers group participation desire
        • Activation: Strong exclusivity motivation (8.8/10)

    3.3 Variant 3 Breakdown
        • Principles: Narrative Transportation + Collective Identity
        • Cognitive Impact: Establishes story investment
        • Activation: High community engagement drive (8.7/10)

4. Engagement Metrics Prediction
    4.1 Quantitative Predictions
        • Engagement Rate: 87-92%
        • Retention Probability: 85% (first 5 episodes)
        • CTA Response: 32-38% activation

    4.2 Qualitative Impact
        • Emotional Resonance: High mystery-driven engagement
        • Social Sharing: Strong viral potential (8.4/10)
        • Community Building: Excellent investigation community formation"""
                },
                'comedy': {
                    'variants': [
                        'Behind the laughter lies genius. [Podcast Name] reveals comedic masterminds—exclusive stories dropping.',
                        'The punchline revolution is here. [Podcast Name] crafts legendary moments—catch the wave now.',
                        'Listeners can\'t contain their reactions. [Podcast Name] delivers mind-bending humor—join the phenomenon.'
                    ],
                    'analysis': """1. LIWC Framework Analysis
    1.1 Word Category Breakdown
        • Cognitive Process Words:
          - Insight: "genius" (95th percentile), "crafts" (88th percentile)
          - Causation: "delivers" (82nd percentile)
          - Discrepancy: "mind-bending" (94th percentile)
        • Emotional Process Words:
          - Positive: "laughter" (96th percentile), "legendary" (90th percentile)
          - Excitement: "revolution" (85th percentile)
        • Social Process Words:
          - Group References: "listeners" (92nd percentile)
          - Status Words: "masterminds" (94th percentile)

    1.2 Linguistic Style Markers
        • Authenticity Indicators: 92nd percentile (genuine enthusiasm)
        • Cognitive Complexity: 88th percentile
        • Temporal Focus: Strong present orientation

2. Pennebaker Psychological Framework
    2.1 Emotional Expression Analysis
        • Emotional Tone: High positive valence (8.8/10)
        • Disclosure Pattern: Escalating excitement structure
        • Authenticity Markers: Natural humor appreciation

    2.2 Cognitive Processing Indicators
        • Analytical Thinking: 82nd percentile
        • Complexity Markers: Sophisticated humor framing
        • Insight Signals: Strong entertainment value patterns

3. Variant-Specific Technique Analysis
    3.1 Variant 1 Breakdown
        • Principles: Status-Expertise + Mystery
        • Cognitive Impact: Creates admiration and curiosity
        • Activation: High entertainment seeking (9.0/10)

    3.2 Variant 2 Breakdown
        • Principles: Zeitgeist + FOMO
        • Cognitive Impact: Triggers trend participation
        • Activation: Strong social inclusion drive (8.9/10)

    3.3 Variant 3 Breakdown
        • Principles: Social Proof + Phenomenal Experience
        • Cognitive Impact: Establishes must-see status
        • Activation: High sharing motivation (9.2/10)

4. Engagement Metrics Prediction
    4.1 Quantitative Predictions
        • Engagement Rate: 90-95%
        • Retention Probability: 88% (first 5 episodes)
        • CTA Response: 35-42% activation

    4.2 Qualitative Impact
        • Emotional Resonance: High positive contagion
        • Social Sharing: Excellent viral potential (9.2/10)
        • Community Building: Strong humor community formation"""
                },
                'business': {
                    'variants': [
                        'Behind closed boardrooms, titans whisper. [Podcast Name] reveals industry secrets—exclusive insights unlocked.',
                        'The paradigm shift begins here. [Podcast Name] decodes success patterns—pioneering minds gather.',
                        'Insiders are betting on tomorrow. [Podcast Name] tracks breakthrough strategies—your advantage awaits.'
                    ],
                    'analysis': """LIWC Analysis:
- Cognitive process words: "decodes" (insight), "patterns" (analytical), "strategies" (achievement)
- Power words: "titans," "paradigm," "breakthrough" (power dynamics)
- Future focus: "betting on tomorrow," "awaits" (future orientation)

Pennebaker Framework:
- High clout indicators in language choice
- Strong analytical thinking patterns
- Future-oriented temporal focus

Psychological Techniques:
Variant 1: Exclusivity principle + information gap theory
Variant 2: Change psychology + collective expertise
Variant 3: Social proof + future-pacing technique

Impact Prediction:
- Credibility: High (90%) based on authority markers
- Action potential: Strong due to future benefit framing
- Knowledge gap closure motivation: Very high

Psycholinguistic Patterns:
- Elevated power word frequency (LIWC power category)
- High analytical thinking score (>90th percentile)
- Strong future temporal orientation"""
                },
                'politics': {
                    'variants': [
                        'Behind the headlines lies truth. [Podcast Name] decodes power dynamics—exclusive revelations emerge.',
                        'The political chess match unfolds. [Podcast Name] maps strategic moves—witness history forming.',
                        'Insiders are connecting dots. [Podcast Name] reveals hidden agendas—join the informed circle.'
                    ],
                    'analysis': """LIWC Analysis:
- Cognitive process words: "decodes," "maps," "connecting" (analytical thinking)
- Power words: "truth," "strategic," "informed" (power dynamics)
- Insight words: "reveals," "hidden," "connecting" (cognitive processing)

Pennebaker Framework:
- High analytical thinking indicators
- Strong power dynamic markers
- Complex cognitive processing patterns

Psychological Techniques:
Variant 1: Truth-seeking motivation + exclusivity
Variant 2: Strategic tension + temporal immediacy
Variant 3: In-group formation + information hierarchy

Impact Prediction:
- Critical thinking activation: High (85-90%)
- Information processing depth: Deep engagement
- Group identity formation: Strong in-group dynamics

Psycholinguistic Patterns:
- High analytical language score (LIWC thinking category)
- Strong power and status markers
- Complex cognitive processing indicators"""
                },
                'ai': {
                    'variants': [
                        'Behind the algorithms lies humanity. [Podcast Name] decodes digital evolution—breakthrough insights emerge.',
                        'The AI revolution has blind spots. [Podcast Name] illuminates hidden patterns—pioneer the future.',
                        'Tech leaders are raising alarms. [Podcast Name] investigates AI impacts—shape tomorrow today.'
                    ],
                    'analysis': """LIWC Analysis:
- Technology words: "algorithms," "digital," "AI" (technical focus)
- Cognitive process words: "decodes," "illuminates," "investigates" (insight)
- Future-oriented words: "evolution," "future," "tomorrow" (temporal focus)

Pennebaker Framework:
- High analytical thinking patterns
- Strong future temporal orientation
- Complex problem-solving indicators

Psychological Techniques:
Variant 1: Humanization of technology + insight revelation
Variant 2: Problem-solution framework + pioneering motivation
Variant 3: Authority principle + urgency activation

Impact Prediction:
- Technical engagement: High (85-90%)
- Future orientation: Strong future-focused thinking
- Action motivation: High due to urgency framing

Psycholinguistic Patterns:
- Elevated technical language frequency
- High cognitive complexity score
- Strong future temporal markers"""
                },
                'boxing': {
                    'variants': [
                        'Behind the glory lies strategy. [Podcast Name] decodes championship mindsets—witness greatness unfold.',
                        'The ring holds untold stories. [Podcast Name] reveals fighter journeys—experience triumph now.',
                        'Champions are rewriting history. [Podcast Name] tracks rising legends—join the revolution.'
                    ],
                    'analysis': """LIWC Analysis:
- Achievement words: "glory," "championship," "triumph" (achievement focus)
- Motion words: "unfold," "rising," "rewriting" (dynamic action)
- Power words: "champions," "greatness," "legends" (status/power)

Pennebaker Framework:
- High achievement motivation markers
- Strong narrative transportation indicators
- Dynamic action orientation patterns

Psychological Techniques:
Variant 1: Achievement motivation + strategic insight
Variant 2: Narrative immersion + temporal urgency
Variant 3: Social proof + movement participation

Impact Prediction:
- Motivation activation: Very high (90-95%)
- Story engagement: Strong narrative pull
- Community participation: High movement joining rate

Psycholinguistic Patterns:
- High achievement word frequency (LIWC achievement category)
- Strong power and status markers
- Dynamic action orientation"""
                }
            }
            return mock_responses.get(theme.lower(), {
                'variants': ['No variants available for this theme.'] * 3,
                'analysis': 'No analysis available for this theme.'
            })

        # Make API call to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional podcast script writer and psychological analyst for Bauer Media Audio, expert in LIWC, Pennebaker's research, psycholinguistics, and advanced psychological engagement techniques. You specialize in structured psychological analysis and evidence-based content optimization."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        # Parse the response to extract variants and analysis
        content = response.choices[0].message.content.strip()
        parts = content.split('\n\n')
        variants = [parts[0], parts[1], parts[2]] if len(parts) > 2 else ["Error parsing variants"] * 3
        analysis = '\n'.join(parts[3:]) if len(parts) > 3 else "Analysis not available"
        
        return {
            'variants': variants,
            'analysis': analysis
        }
    
    except Exception as e:
        return {
            'variants': [f"Error generating intro: {str(e)}"] * 3,
            'analysis': "Error in analysis generation."
        }

# Uncomment for AWS Polly TTS integration
"""
def generate_tts(text, voice_id='Joanna'):
    polly = boto3.client(
        'polly',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name='eu-west-1'
    )
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id
    )
    return response['AudioStream'].read()
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    intros = None
    if request.method == 'POST':
        theme = request.form.get('theme', '').strip()
        if theme:
            intros = generate_podcast_intros(theme)
    return render_template('index.html', intros=intros)

if __name__ == '__main__':
    app.run(debug=True) 
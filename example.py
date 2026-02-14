"""
Example Usage of EchoScan Engine
Demonstrates how to use the EchoScan Multilingual Intelligence Engine
"""

import json
from echoscan import EchoScan, TranscriptSegment, Category

def demo_with_mock_data():
    """
    Demonstrates EchoScan with mock data
    (Useful until audio transcription is fully implemented)
    """
    print("=" * 60)
    print("EchoScan Multilingual Intelligence Engine - Demo")
    print("=" * 60)
    
    # Initialize engine with Tamil as target language
    engine = EchoScan(target_language="Tamil")
    
    # Mock transcript segments (simulating transcribed audio)
    mock_segments = [
        {
            "start_time": 0.0,
            "end_time": 3.5,
            "text": "Hello everyone, let's start the meeting",
            "category": Category.INFORMATION.value
        },
        {
            "start_time": 3.5,
            "end_time": 7.2,
            "text": "We need to complete the project report by Friday",
            "category": Category.URGENT.value
        },
        {
            "start_time": 7.2,
            "end_time": 11.0,
            "text": "Um, you know, we should also schedule a follow-up meeting",
            "category": Category.ACTIONABLE.value
        },
        {
            "start_time": 11.0,
            "end_time": 13.5,
            "text": "Like, um, the client mentioned some feedback",
            "category": Category.FILLER.value
        },
        {
            "start_time": 13.5,
            "end_time": 18.0,
            "text": "Please review the documentation immediately",
            "category": Category.URGENT.value
        }
    ]
    
    # Manually create output (simulating full pipeline)
    output = {
        "summary": "[Tamil] இந்த சந்திப்பில் திட்ட அறிக்கையை வெள்ளிக்கிழமைக்குள் முடிக்க வேண்டும் என்று விவாதிக்கப்பட்டது. ஆவணங்களை உடனடியில் மதிப்பாய்வு செய்ய வேண்டும் மற்றும் பின்தொடர்தல் கூட்டத்தை திட்டமிட வேண்டும்.",
        "action_items": [
            "[Tamil] திட்ட அறிக்கையை வெள்ளிக்கிழமைக்குள் முடிக்கவும்",
            "[Tamil] பின்தொடர்தல் கூட்டத்தை திட்டமிடவும்",
            "[Tamil] ஆவணங்களை உடனடியாக மதிப்பாய்வு செய்யவும்"
        ],
        "transcript_segments": [
            {
                "start_time": seg["start_time"],
                "end_time": seg["end_time"],
                "original_english": seg["text"],
                "translated_text": f"[Tamil Translation] {{seg['text']}}",
                "category": seg["category"]
            }
            for seg in mock_segments
        ]
    }
    
    # Output as raw JSON (no preamble, as per specification)
    json_output = json.dumps(output, ensure_ascii=False, indent=2)
    print("\n" + json_output)
    print("\n" + "=" * 60)
    
    # Show category breakdown
    print("\nCategory Breakdown:")
    for category in Category:
        count = sum(1 for seg in mock_segments if seg["category"] == category.value)
        print(f"  {{category.value}}: {{count}} segments")

def demo_categorization():
    """
    Demonstrates the categorization logic
    """
    print("\n" + "=" * 60)
    print("Category Detection Demo")
    print("=" * 60 + "\n")
    
    engine = EchoScan(target_language="Tamil")
    
    test_sentences = [
        "We need this done ASAP, it's urgent",
        "Um, you know, like, well...",
        "The project status is progressing well",
        "Please complete your tasks by end of day",
        "This is critical information for the deadline"
    ]
    
    mock_segments = [
        {"text": sentence, "start_time": i * 5.0, "end_time": (i + 1) * 5.0}
        for i, sentence in enumerate(test_sentences)
    ]
    
    categorized = engine._categorize_segments(mock_segments)
    
    for seg in categorized:
        print(f"Text: '{{seg['text']}}'")
        print(f"Category: '{{seg['category']}}'")
        print("-" * 60)

if __name__ == "__main__":
    # Run demos
    demo_with_mock_data()
    demo_categorization()
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Configure API keys in config.json")
    print("3. Implement audio transcription in echoscan.py")
    print("4. Implement translation in echoscan.py")
    print("5. Test with real audio files")
    print("=" * 60)

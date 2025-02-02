from streamlit.testing.v1 import AppTest

def test_app_initialization():
    at = AppTest.from_file("main.py")
    at.run()
    
    # Check if the title is correct
    assert at.title[0].value == "Hi!"
    
    # Check if the text input for API key exists
    assert len(at.text_input) == 1
    assert at.text_input[0].label == "Please enter your OpenRouter API key:"
    
    # Check if the warning message is displayed when no API key is provided
    assert len(at.warning) == 1
    assert at.warning[0].value == "API key is required to use this application."

def test_chat_interaction():
    at = AppTest.from_file("main.py")
    at.run()
    
    # Check if text input exists
    assert len(at.text_input) > 0
    
    # Simulate entering an API key
    at.text_input[0].set_value("dummy_api_key").run()
    
    # Check if chat input exists after entering API key
    assert len(at.chat_input) > 0

def test_session_state():
    at = AppTest.from_file("main.py")
    at.run()

    # Simulate entering an API key to trigger session state initialization
    assert len(at.text_input) > 0
    at.text_input[0].set_value("dummy_api_key").run()

    # Check if session state is initialized correctly
    assert "llm" in at.session_state, f"Session state keys: {at.session_state.keys()}"
    assert at.session_state["llm"] == "meta-llama/llama-3.2-3b-instruct:free"
    assert "messages" in at.session_state
    assert at.session_state["messages"] == []
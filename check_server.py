"""Quick script to check if server is running"""
import requests
import time

def check_server():
    try:
        response = requests.get('http://127.0.0.1:8000/', timeout=2)
        print("✅ Server is RUNNING!")
        print(f"Response: {response.json()}")
        print("\n🌐 Open in your browser:")
        print("   http://127.0.0.1:8000/docs")
        print("\n📝 Test a query:")
        print('   {"query": "Why did I get only 25% refund for order ORD001?"}')
        return True
    except requests.exceptions.ConnectionError:
        print("⏳ Server is starting...")
        print("   Please wait a few more seconds and try again")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("Checking server status...")
    print("=" * 50)
    check_server()



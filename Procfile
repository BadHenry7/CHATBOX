# services:
#   - type: web
#     name: rasa-chatbox
#     env: docker
#     plan: free
#     branch: main
#     dockerfilePath: Dockerfile
#     region: oregon
web: rasa run --enable-api --cors "*" --debug --port $PORT --model models/20250313-160938-corn-hour.tar.gz

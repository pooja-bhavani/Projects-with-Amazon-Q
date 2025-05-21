from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.programming.framework import React
from diagrams.onprem.database import MongoDB
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Nginx
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.network import CloudFront
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS
from diagrams.aws.security import Cognito
from diagrams.generic.device import Mobile, Tablet

with Diagram("RoadRash Game Architecture", show=False, direction="LR", filename="roadrash_architecture"):
    
    # Client devices
    with Cluster("Game Clients"):
        clients = [
            Mobile("Mobile Client"),
            Tablet("Desktop Client")
        ]
    
    # Frontend
    with Cluster("Game Frontend"):
        frontend = React("Game UI")
        assets_cdn = CloudFront("Assets CDN")
    
    # Backend Services
    with Cluster("Game Backend"):
        api_gateway = Nginx("API Gateway")
        
        with Cluster("Core Game Services"):
            game_server = Server("Game Server")
            physics_engine = Python("Physics Engine")
            ai_engine = Python("AI Engine")
            
        with Cluster("Supporting Services"):
            auth_service = Cognito("Authentication")
            leaderboard = Lambda("Leaderboard")
            matchmaking = Lambda("Matchmaking")
    
    # Data Storage
    with Cluster("Data Storage"):
        game_db = MongoDB("Game Database")
        player_db = Dynamodb("Player Profiles")
        assets_storage = S3("Game Assets")
    
    # Real-time Communication
    with Cluster("Real-time Services"):
        event_bus = Kafka("Event Bus")
        notification = SNS("Notifications")
    
    # Connect components
    clients >> frontend
    clients >> assets_cdn
    frontend >> api_gateway
    
    api_gateway >> auth_service
    api_gateway >> game_server
    
    game_server >> physics_engine
    game_server >> ai_engine
    game_server >> event_bus
    
    game_server >> game_db
    auth_service >> player_db
    assets_cdn >> assets_storage
    
    event_bus >> notification
    event_bus >> leaderboard
    event_bus >> matchmaking
    
    matchmaking >> game_server

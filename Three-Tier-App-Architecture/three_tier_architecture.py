#!/usr/bin/env python3
from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, Lambda
from diagrams.aws.database import RDS, DynamoDB
from diagrams.aws.integration import SQS, EventBridge
from diagrams.aws.network import APIGateway, ELB
from diagrams.aws.security import Cognito

with Diagram("Microservices Architecture", show=False):
    
    # API Gateway and Authentication
    api = APIGateway("API Gateway")
    auth = Cognito("Authentication")
    
    # Event Bus
    events = EventBridge("Event Bus")
    
    with Cluster("Frontend Services"):
        lb = ELB("Load Balancer")
        web_services = [
            ECS("Web Service 1"),
            ECS("Web Service 2")
        ]
        
        lb >> web_services
    
    with Cluster("Backend Services"):
        user_service = ECS("User Service")
        order_service = ECS("Order Service")
        payment_service = ECS("Payment Service")
        notification = Lambda("Notification")
        
        queue = SQS("Message Queue")
        
        order_service >> queue >> notification
    
    with Cluster("Data Layer"):
        user_db = RDS("User Database")
        order_db = RDS("Order Database")
        cache = DynamoDB("Cache")
        
    # Connect components
    api >> auth
    api >> lb
    api >> [user_service, order_service, payment_service]
    
    user_service >> user_db
    order_service >> order_db
    payment_service >> order_db
    
    [user_service, order_service, payment_service] >> events
    events >> notification
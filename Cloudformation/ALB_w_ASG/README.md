# Application Load Balancer with AutoScaling Group
### Cloudformation Template

#### Template Checklist
- VPC
- Public Subnet (dep of LB)
- Autoscaling Group
- Web Server(s)
- Web Server Security Group
- Internet Gateway
- Route Table
- ALB
- ALB Listener
- ALB Target Group
- ALB Security Group
- Launch Configuration (dep of ASG)
- VPCGatewayAttachment
- SubnetRouteTableAssociation
- Route
- Network ACL
- NACL - Ingress
- NACL - Egress
- SubnetNetworkAclAssociation

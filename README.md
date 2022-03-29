# SpringCloud-Function-SPEL-
poc of SpringCloud Function SPEL漏洞        
Spring Cloud Function 是基于Spring Boot 的函数计算框架，通过对传输细节和基础架构进行抽象，为开发人员保留熟悉的开发工具和开发流程，使开发人员专注在实现业务逻辑上，从而提升开发效率。
访问Spring Cloud Function的 HTTP请求头中存在 spring.cloud.function.routing-expression参数，其 SpEL表达式可进行注入攻击，并通过 StandardEvaluationContext解析执行。最终，攻击者可通过该漏洞进行远程命令执行。        
分析文章推荐：https://www.cnblogs.com/wh4am1/p/16062306.html

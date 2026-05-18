"""
AI 多 Agent 法律文书智能生成与校验系统 - 可运行演示
"""

from agents import RequirementAgent, LegalRetrievalAgent, ReasoningAgent, GenerationAgent, ReviewAgent

def main():
    print("=" * 50)
    print("法律文书多 Agent 协作系统启动")
    print("=" * 50)

    # 模拟用户输入
    user_input = """
    合同类型: 软件开发服务合同
    甲方: 某科技公司
    乙方: 某外包开发团队
    项目金额: 200万元
    交付期限: 6个月
    特殊要求: 源代码知识产权归甲方，乙方需保密
    """

    # 1. 需求理解 Agent
    req_agent = RequirementAgent()
    structured_req = req_agent.extract(user_input)
    print("\n[1] 需求理解 Agent 提取结果:")
    print(structured_req)

    # 2. 法规检索 Agent
    legal_agent = LegalRetrievalAgent()
    legal_info = legal_agent.search(structured_req["keywords"])
    print("\n[2] 法规检索 Agent 找到相关法规:")
    for law in legal_info:
        print(f"  - {law}")

    # 3. 推理 Agent
    reasoning_agent = ReasoningAgent()
    risk_analysis = reasoning_agent.analyze(structured_req, legal_info)
    print("\n[3] 逻辑推理 Agent 风险分析:")
    print(f"  冲突检测: {risk_analysis['conflicts']}")
    print(f"  建议: {risk_analysis['suggestions']}")

    # 4. 生成 Agent
    gen_agent = GenerationAgent()
    draft = gen_agent.generate_draft(structured_req, risk_analysis)
    print("\n[4] 文书生成 Agent 生成草案 (前200字符):")
    print(draft[:200] + "...")

    # 5. 审阅 Agent
    review_agent = ReviewAgent()
    review_result = review_agent.review(draft)
    print("\n[5] 审阅 Agent 输出:")
    print(f"  风险等级: {review_result['risk_level']}")
    print(f"  修改建议: {review_result['comments'][0] if review_result['comments'] else '无'}")

    print("\n" + "=" * 50)
    print("多 Agent 协作流程完成")
    print("=" * 50)

if __name__ == "__main__":
    main()

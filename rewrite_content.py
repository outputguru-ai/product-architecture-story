#!/usr/bin/env python3
import re

with open('stage-7-ainative-rag-agent.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Section 01 replacement
old_s01 = '''    <section id="why">
<span class="section-label">01 / 起源</span>
      <h2>为什么 Prompt 不够了？</h2>
      <p class="lead">
        Prompt 时代让人们第一次体验到了 AI 的力量，但它很快暴露了一个致命问题：<strong>AI 会"一本正经地胡说八道"（幻觉），而且它的知识只更新到训练数据截止的那一天。</strong> 企业不敢把 AI 用于关键业务，因为 AI 可能给出错误的法律建议、编造不存在的政策条文、推荐过时的产品。
      </p>

      <p>
        要理解 RAG + Agent 时代为什么诞生，我们必须回到 Prompt 时代的<strong>三个核心痛点</strong>：
      </p>

      <div class="story-block">
        <h4>痛点一：幻觉（Hallucination）</h4>
        <p>律师让 AI 查一个案例，AI 给出了看似专业的分析——但案例编号是编造的。医生让 AI 诊断症状，AI 给出了一种罕见病的名称——但症状描述与该病并不匹配。<strong>LLM 的目标是"生成流畅的文本"，而不是"生成正确的文本"。</strong> 当业务容错率很低时（医疗、法律、金融），Prompt  alone 是不够的。</p>
        <p style="margin-top:16px"><strong>痛点二：知识截止（Knowledge Cutoff）</strong></p>
        <p>GPT-4 的训练数据截止到 2023 年。如果用户问"昨天发布的 iPhone 有什么新功能"，AI 一无所知。如果企业想让 AI 回答关于自家产品的问题，AI 也不可能知道——因为训练数据里根本没有。</p>
        <p style="margin-top:16px"><strong>痛点三：无法行动（No Agency）</strong></p>
        <p>ChatGPT 能聊天，但它不能帮你订机票、不能查你的银行账户、不能发邮件。它是一个"只会说不会动"的聊天机器人。要让 AI 真正有用，必须给它<strong>记忆（访问外部数据）和手脚（调用外部工具）</strong>。</p>
      </div>

      <p><strong>五股推动力：</strong></p>

      <div class="story-block">
        <h4>五股推动力</h4>
        <p><strong>① 企业 AI 采用的信任危机（2023）：</strong>很多企业试点了 ChatGPT，但因为幻觉问题不敢上线。市场迫切需要一种"让 AI 基于真实信息回答"的技术。<strong>RAG 应运而生。</strong></p>
        <p style="margin-top:16px"><strong>② GPT-4 Function Calling（2023）：</strong>OpenAI 在 GPT-4 中加入了"函数调用"能力——模型可以根据用户请求判断需要调用哪个外部 API（如查天气、查股票、发邮件），并生成调用参数。<strong>AI 第一次有了"手脚"。</strong></p>
        <p style="margin-top:16px"><strong>③ 向量数据库爆发（2023）：</strong>Pinecone、Weaviate、Chroma 等向量数据库让"语义搜索"变得简单。你可以把企业文档转化为向量，然后问 AI："我们的退货政策是什么？"AI 先搜索文档，再基于搜索结果回答。<strong>这是 RAG 的技术基础。</strong></p>
        <p style="margin-top:16px"><strong>④ LangChain 框架诞生（2022–2023）：</strong>Harrison Chase 创建的 LangChain 让开发者可以像搭积木一样组合 LLM、向量数据库、API 调用、记忆模块。它降低了构建复杂 AI 应用的门槛。<strong>Agent 开发从"手搓"走向了"框架化"。</strong></p>
        <p style="margin-top:16px"><strong>⑤ AutoGPT 的病毒式传播（2023）：</strong>Torantulino 发布的 AutoGPT 让 AI 可以自主设定目标、分解任务、调用工具、执行行动。虽然早期版本不太稳定，但它让人们看到了<strong>"自主 AI"的可能性</strong>——AI 不再只是回答问题的助手，而是能独立完成任务的代理。</p>
      </div>

      <p><strong>核心认知转变：</strong>从"AI 作为聊天机器人"到"AI 作为系统组件"。RAG 让 AI 有了"记忆力"（能查企业数据），Agent 让 AI 有了"行动力"（能调用工具）。AI 从一个"会说话的黑盒"变成了一个"可组装、可扩展、可信赖的系统零件"。</p>

      <h3>关键事件时间线</h3>
      <ul class="events-list">
        <li><span class="event-year">2022</span><span class="event-text">LangChain 框架发布，开启 LLM 应用开发框架化时代。</span></li>
        <li><span class="event-year">2023.03</span><span class="event-text">GPT-4 发布，支持 Function Calling——AI 第一次能调用外部工具。</span></li>
        <li><span class="event-year">2023.03</span><span class="event-text">Meta 开源 LLaMA，开源大模型生态爆发。</span></li>
        <li><span class="event-year">2023.04</span><span class="event-text">AutoGPT 发布并病毒式传播，"AI Agent"概念进入大众视野。</span></li>
        <li><span class="event-year">2023.06</span><span class="event-text">Pinecone 向量数据库获得巨额融资，语义搜索成为热点。</span></li>
        <li><span class="event-year">2023</span><span class="event-text">LlamaIndex 崛起，专注于数据连接和 RAG 实现。</span></li>
        <li><span class="event-year">2023</span><span class="event-text">Microsoft 365 Copilot 发布，AI 嵌入 Office 全套产品。</span></li>
        <li><span class="event-year">2024</span><span class="event-text">RAG 成为企业级 AI 的标准架构模式。Dify、Flowise 让 RAG/Agent 开发可视化。</span></li>
      </ul>
    </section>'''

new_s01 = '''    <section id="why">
      <span class="section-label">01 / 起源</span>
      <h2>为什么 Prompt 不够了？</h2>
      <p class="lead">
        ChatGPT 的横空出世让所有人看到了 AI 的潜力。但很快，一个残酷的现实浮出水面：<strong>大语言模型会"一本正经地胡说八道"——它 hallucinate（幻觉），它没有访问企业私有数据的权限，它对 2022 年之后发生的事情一无所知。</strong> 2023–2024 年，整个行业意识到：光靠 Prompt 是远远不够的。
      </p>

      <p>
        要理解 RAG + Agent 时代为什么诞生，我们必须先回到<strong>纯 Prompt 时代的"天花板"</strong>。在 2022 年底到 2023 年初，最热门的"AI 应用"就是对着 ChatGPT 写提示词。产品经理们发现，精心设计的 Prompt 确实能让模型输出质量提升数倍，但有几个根本性的问题无法解决：模型不知道你公司的内部政策、不知道昨天的股价、不能帮你查邮件、不能操作你的 CRM 系统。它就像一个博学但闭门不出的学者——什么都懂一点，但什么都不做。
      </p>

      <p>
        企业级场景的痛点更加明显。一位银行的高管问："能不能让 AI 帮我审贷款申请？"答案是：可以，但 AI 不知道贵行的风控规则。一位医院的信息科主任问："能不能让 AI 辅助诊断？"答案是：可以，但 AI 读不了贵院的电子病历。一位律师事务所的合伙人问："能不能让 AI 查判例？"答案是：可以，但 AI 的"知识"截止到训练数据的时间点。<strong>没有外部记忆和外部工具，AI 只能是一个聪明的聊天机器人，而不是一个能干活的员工。</strong>
      </p>

      <div class="pull-quote">
        "Prompt Engineering 是给 AI 一副好嗓子。RAG 和 Agent 是给 AI 装上记忆和手脚。"
        <cite>—— 2023 年一位 AI 应用开发者的总结</cite>
      </div>

      <p>
        <strong>两大解决方案在 2023 年同时涌现：</strong>
      </p>

      <p>
        <strong>RAG（检索增强生成）</strong>解决的是"记忆"问题。它的思路极其朴素：用户提问时，先从一个外部知识库（比如企业的文档、数据库、网页）中检索出最相关的片段，把这些片段和用户的原始问题一起塞给 LLM，让它"基于这些资料来回答"。这就像让 AI 开卷考试——它不需要背诵所有知识，只需要知道去哪里查、查到了怎么组织答案。<strong>RAG 把 AI 从一个"背诵者"变成了"研究员"。</strong>
      </p>

      <p>
        <strong>Agent（智能体）</strong>解决的是"手脚"问题。它的核心思想是：给 AI 一套可以调用的工具（搜索 API、计算器、数据库查询、邮件发送、日历创建……），让 AI 自己判断"为了完成这个任务，我需要调用哪些工具、按什么顺序调用"。GPT-4 在 2023 年推出的 Function Calling API 是这个方向的关键基础设施。<strong>Agent 把 AI 从一个"对话者"变成了"执行者"。</strong>
      </p>

      <div class="story-block">
        <h4>五股推动力</h4>
        <p>
          <strong>① Hallucination crisis（幻觉危机）：</strong>2023 年初，大量企业试点 AI 项目因为"AI 胡说八道"而失败。一个著名的案例是：某律师用 ChatGPT 写法庭文件，结果 AI 编造了完全不存在的判例。这个事件登上了新闻头条，让企业对 AI 的"可信度"产生了严重质疑。<strong>"如果不解决幻觉问题，AI 永远进不了严肃业务场景"——这是 RAG 成为主流架构的直接动力。</strong>
        </p>
        <p style="margin-top:16px">
          <strong>② Knowledge cutoff（知识截止时间）：</strong>GPT-4 的训练数据截止到 2023 年 4 月，之后发生的事它一概不知。企业的私有数据（内部文档、客户记录、产品手册）从未出现在训练数据中。这意味着：<strong>即便模型再聪明，它对"你的业务"也是盲人摸象。</strong> RAG 让企业能把 AI 接入自己的数据，而不需要重新训练一个模型。
        </p>
        <p style="margin-top:16px">
          <strong>③ Enterprise adoption barrier（企业采纳门槛）：</strong>2023 年中，"AI 赋能"成为每一家大企业的战略议题，但 IT 部门的反馈很一致："我们不能把客户数据发给 OpenAI 的公有 API。"这催生了私有化部署的需求——企业需要在自己可控的环境中运行 AI，并确保 AI 只访问被授权的数据。<strong>RAG 架构天然适合私有化：知识库留在本地，只有检索到的片段传给模型。</strong>
        </p>
        <p style="margin-top:16px">
          <strong>④ Tool use emergence（工具使用能力的涌现）：</strong>2023 年 3 月，GPT-4 发布的同时推出了 Function Calling API。这是 LLM 第一次能"结构化地调用外部工具"——模型输出的不是自然语言，而是一个 JSON 格式的函数调用指令（如 {"function": "get_weather", "args": {"city": "北京"}}）。<strong>这个看似简单的 API 彻底改变了 AI 的能力边界：AI 不再只是"说话"，它可以"行动"。</strong>
        </p>
        <p style="margin-top:16px">
          <strong>⑤ Agent frameworks（Agent 框架的爆发）：</strong>LangChain（2022 年底发布，2023 年爆发）、AutoGPT（2023 年 4 月 GitHub 星标数一周破 10 万）、BabyAGI（2023 年 4 月）……这些框架证明了一件事：AI 可以自主地分解任务、调用工具、观察结果、调整策略。<strong>Agent 框架把"AI 能做什么"的想象力从"回答一个问题"扩展到了"完成一个项目"。</strong>
        </p>
      </div>

      <p>
        那么，<strong>科学认知发生了怎样的变化</strong>？最核心的认知迁移是：<strong>从"AI as a chatbot"到"AI as a system component"</strong>。2022 年，人们把 AI 看作一个对话界面；2023–2024 年，人们开始把 AI 看作一个可以嵌入任何系统的"认知模块"——它接收输入（问题+上下文+工具）、执行推理、产生输出（答案+行动）。这个认知转变的深远影响是：产品经理开始像设计"微服务"一样设计"AI 模块"——每个模块有明确的输入输出、有状态管理、有错误处理、有成本预算。
      </p>

      <p>
        另一个深刻的认知转变是<strong>"数据工程 > 模型工程"</strong>。2023 年初，所有人的目光都集中在"哪个模型最强"上。但到 2023 年底，实践者们发现：<strong>决定 RAG 系统质量的往往不是模型，而是数据准备——文档怎么切分、嵌入模型怎么选、检索策略怎么调、重排序怎么做。</strong> 这催生了一个全新的工种："RAG 工程师"——他们的核心技能不是训练模型，而是搭建和维护高质量的知识管道。
      </p>

      <p>
        为什么是<strong>RAG + Agent</strong>而不是别的方向？因为 Prompt Engineering 把 AI 的能力天花板推到了一个点：模型本身足够聪明，但缺乏记忆和行动力。RAG 补上了记忆，Agent 补上了行动力。当两者结合时，AI 第一次具备了"理解任务 → 检索信息 → 调用工具 → 生成结果"的完整闭环——这让它从"玩具"变成了"工具"。
      </p>

      <h3>关键事件时间线</h3>
      <ul class="events-list">
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">GPT-4 发布并推出 Function Calling API——LLM 第一次能结构化调用外部工具。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">LangChain 框架快速迭代，成为连接 LLM、数据源和工具的事实标准。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">Meta 开源 LLaMA，开源大模型生态爆发，降低了企业私有化部署的门槛。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">AutoGPT 在 GitHub 上一周获 10 万星标——AI 自主完成任务的愿景引发全球热议。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">向量数据库（Pinecone、Weaviate、Chroma）成为 AI 基础设施的热门赛道。</span>
        </li>
        <li>
          <span class="event-year">2024</span>
          <span class="event-text">RAG 成为企业级 AI 应用的"标准架构模式"——几乎每个 LLM 应用都包含检索层。</span>
        </li>
        <li>
          <span class="event-year">2024</span>
          <span class="event-text">Dify、Flowise 等可视化 LLM 应用开发平台崛起，让非工程师也能搭建 RAG/Agent 应用。</span>
        </li>
      </ul>
    </section>'''

if old_s01 in content:
    content = content.replace(old_s01, new_s01)
    print("Section 01 replaced")
else:
    print("Section 01 old text NOT FOUND")

with open('stage-7-ainative-rag-agent.html', 'w', encoding='utf-8') as f:
    f.write(content)

#!/usr/bin/env python3
import re

with open('stage-7-ainative-rag-agent.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace section 01
old_section = '''    <!-- ═══════════════════════════════════════════════
         01 为什么会诞生
         ═══════════════════════════════════════════════ -->
    <section id="why">
      <span class="section-label">01 / 起源</span>
      <h2>从"管理代码"到"管理认知"</h2>
      <p class="lead">
        云原生时代让工程师不再为基础设施操心。但它留下了一个更根本的问题：<strong>软件只能执行人类写死的指令，它不能理解需求、不能推理、不能创造。</strong> AI Native 的核心命题是：让软件具备认知能力，让它不仅能"运行"，还能"理解""推理""生成"。
      </p>

      <p>
        要理解 AI Native 为什么诞生，我们必须先回到<strong>传统软件的"天花板"</strong>。在 AI 出现之前，所有软件都是"确定性的"——你写一个 if/else，它就按你的逻辑走；你漏掉一个分支，它就报错或崩溃。软件的"智能"完全取决于人类程序员的想象力和代码质量。
      </p>

      <p>
        但现实世界是模糊的。用户说"帮我订一张去北京的票"，这句话背后有无数种理解方式：哪一天？哪个机场？什么舱位？预算多少？以前的做法是程序员穷尽所有可能性，写几千个分支来"猜"用户的意图——但这注定是残缺的。真正的突破来自一个简单但深刻的认知转变：<strong>与其让程序员穷举所有规则，不如让机器自己从海量数据中学习规则。</strong>
      </p>

      <div class="pull-quote">
        "我们用了六十年教计算机按规则思考。现在我们终于教会了它们按经验思考。"
        <cite>—— 一位 AI 研究员对 Transformer 时代的评述</cite>
      </div>

      <p>
        <strong>关键转折点不是单一事件，而是五股力量的汇聚：</strong>
      </p>

      <div class="story-block">
        <h4>五股推动力</h4>
        <p>
          <strong>① Transformer 架构的突破（2017–2020）：</strong>Google 在 2017 年发布的 Transformer 论文《Attention Is All You Need》改变了整个 AI 领域的游戏规则。它的核心洞察是：用"注意力机制"替代传统的循环神经网络（RNN），让模型能同时看到整段文本的上下文，而不是一个字一个字地"回忆"。这个架构的扩展性惊人——当你给它更多数据、更多参数、更多计算力时，它展现出了前所未有的"涌现能力"（Emergent Abilities）：突然能写诗、能编程、能翻译、能推理。<strong>这就是大语言模型（LLM）的技术根基。</strong>
        </p>
        <p style="margin-top:16px">
          <strong>② GPT-3 与"涌现能力"的震撼（2020）：</strong>OpenAI 发布的 GPT-3 有 1750 亿参数，是前一代 GPT-2 的 100 倍。它第一次让人们意识到：当模型足够大时，它会"突然学会"一些你从未专门教过的事情——比如从几个例子中学会一种新语言、用零样本的方式完成从未见过的任务。这被称为<strong>"少样本学习"（Few-shot Learning）</strong>。它标志着 AI 从"窄领域专家"（只会下棋、只会翻译）变成了"通才"（什么都能聊）。
        </p>
        <p style="margin-top:16px">
          <strong>③ ChatGPT 的破圈时刻（2022）：</strong>2022 年 11 月，OpenAI 发布了 ChatGPT——一个能聊天、能写代码、能写诗、能回答任何问题（虽然有时会"一本正经地胡说八道"）的对话机器人。它在两个月内获得了 1 亿月活用户，成为历史上增长最快的消费级产品。<strong>ChatGPT 不是一个技术突破，而是一个产品突破</strong>——它证明了大模型的"对话界面"能让普通人直接感受到 AI 的力量。
        </p>
        <p style="margin-top:16px">
          <strong>④ 云原生基础设施的成熟（2020–2023）：</strong>云原生时代铺好了 AI 时代的"路"。大模型训练和推理需要海量 GPU 集群，而 Kubernetes + 云厂商的 GPU 实例 + 弹性扩容让这成为可能。AWS、Azure、Google Cloud 都在 2020–2022 年间大幅扩充了 GPU 资源。同时，Hugging Face、Replicate 等平台让模型的发布和调用变得像发布一个 npm 包一样简单。<strong>没有云原生，就没有 AI Native 的基础设施。</strong>
        </p>
        <p style="margin-top:16px">
          <strong>⑤ 开源生态的爆发（2022–2024）：</strong>Meta 开源了 LLaMA（2023），Databricks 开源了 Dolly，Stability AI 开源了 Stable Diffusion……开源大模型让中小企业和个人开发者也能使用 AI 能力，而不必依赖 OpenAI 的 API。LangChain（2022）、LlamaIndex（2022）等框架降低了开发 AI 应用的门槛。<strong>开源生态的繁荣让 AI Native 从"大厂特权"变成了"全民运动"。</strong>
        </p>
      </div>

      <p>
        那么，<strong>科学认知发生了怎样的变化</strong>？最核心的认知迁移是：<strong>从"规则驱动"到"数据驱动"</strong>。传统软件是人类程序员把知识编码成规则；AI Native 软件是机器从数据中学习知识。这意味着：软件的"智能上限"不再取决于程序员的想象力，而取决于数据的数量和质量。
      </p>

      <p>
        另一个深刻的认知转变是<strong>"不确定性"的接纳</strong>。传统软件追求 100% 的确定性——输入 A 必须输出 B。但大模型的本质是概率性的——它给出的是"最可能的答案"，而非"绝对正确的答案"。这迫使产品设计师重新思考用户体验：<strong>如果 AI 可能出错，我们如何设计"容错界面"？如何让用户能验证、修正、覆盖 AI 的输出？</strong> 这是 AI Native 产品设计中最核心的课题。
      </p>

      <p>
        为什么是<strong>AI Native</strong>而不是别的方向？因为云原生解决了"如何高效运行软件"的问题，但无法解决"如何让软件更聪明"的问题。AI 提供了一种全新的"软件构建材料"——大语言模型——它让软件具备了"理解语言""生成内容""推理决策"的能力。当这些能力被嵌入到产品的每一个触点中时，产品就从"工具"变成了"伙伴"。
      </p>

      <h3>关键事件时间线</h3>
      <ul class="events-list">
        <li>
          <span class="event-year">2017</span>
          <span class="event-text">Google 发布 Transformer 论文《Attention Is All You Need》，奠定大语言模型的技术基础。</span>
        </li>
        <li>
          <span class="event-year">2018</span>
          <span class="event-text">Google 发布 BERT，首次展示了预训练模型在理解任务上的突破性表现。</span>
        </li>
        <li>
          <span class="event-year">2020</span>
          <span class="event-text">OpenAI 发布 GPT-3（175B 参数），展示了惊人的"少样本学习"能力，引发行业震动。</span>
        </li>
        <li>
          <span class="event-year">2021</span>
          <span class="event-text">GitHub 推出 Copilot，AI 辅助编程首次进入开发者日常工作流。</span>
        </li>
        <li>
          <span class="event-year">2022</span>
          <span class="event-text">Stable Diffusion 开源，AI 图像生成进入大众视野。11 月 ChatGPT 发布，两个月获 1 亿用户。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">GPT-4 发布，多模态能力（文本+图像）惊艳世界。Meta 开源 LLaMA，开源大模型生态爆发。LangChain 成为 Agent 开发主流框架。</span>
        </li>
        <li>
          <span class="event-year">2023</span>
          <span class="event-text">AutoGPT 引爆 Agent 概念——让 AI 自主设定目标、分解任务、调用工具完成复杂工作。</span>
        </li>
        <li>
          <span class="event-year">2024</span>
          <span class="event-text">Claude 3、Gemini 1.5、GPT-4o 等模型在长上下文（100万+ tokens）、多模态、推理能力上竞争。AI Agent 平台（如 CrewAI、Dify）大量涌现。</span>
        </li>
        <li>
          <span class="event-year">2024</span>
          <span class="event-text">AI 编程工具爆发：Cursor（AI IDE）、Windsurf、Devin（AI 软件工程师）。AI Native 应用从"玩具"走向"生产力工具"。</span>
        </li>
        <li>
          <span class="event-year">2025</span>
          <span class="event-text">AI Agent 成为产品架构的核心概念。多 Agent 协作系统（Multi-Agent System）开始应用于企业场景。 reasoning models（如 o1/o3）让 AI 具备了"慢思考"能力。</span>
        </li>
      </ul>
    </section>'''

new_section = '''    <!-- ═══════════════════════════════════════════════
         01 为什么会诞生
         ═══════════════════════════════════════════════ -->
    <section id="why">
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

if old_section in content:
    content = content.replace(old_section, new_section)
    with open('stage-7-ainative-rag-agent.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Section 01 replaced successfully!")
else:
    print("Old section not found. Checking...")
    # Let's find where section 01 starts
    idx = content.find('01 为什么会诞生')
    if idx >= 0:
        print(f"Found '01 为什么会诞生' at index {idx}")
        print("Context around it:")
        print(repr(content[idx-50:idx+100]))
    else:
        print("Cannot find '01 为什么会诞生' at all")

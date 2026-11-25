<h1 align="center">A Survey on AI for AI: When the Improver Becomes the Improvee</h1>

<p align="center">Deheng Ye · Zheng Zhang · Hao Wang · Chunyan Miao</p>

<p align="center">
  <a href="#papers"><img src="https://img.shields.io/badge/Paper_catalog-193d63?style=for-the-badge" alt="Browse the papers in this README"></a>
  <a href="https://3dagentworld.github.io/awesome-ai-for-ai/papers.html"><img src="https://img.shields.io/badge/Paper_browser-28645e?style=for-the-badge" alt="Search and filter papers"></a>
  <a href="https://doi.org/10.20944/preprints202609.0591.v2"><img src="https://img.shields.io/badge/Preprint-536982?style=for-the-badge" alt="Read the preprint"></a>
  <a href="#citation"><img src="https://img.shields.io/badge/BibTeX-536982?style=for-the-badge" alt="Get the BibTeX citation"></a>
</p>

<p align="center">
  <img src="assets/fig-taxonomy.png" width="720" alt="The AI for AI taxonomy groups work by experience providers, evaluation providers, and change producers.">
</p>

<p align="center">
  <a href="https://3dagentworld.github.io/awesome-ai-for-ai/">Project page</a> · <a href="https://3dagentworld.github.io/awesome-ai-for-ai/paper.html">Full survey</a> · <a href="#suggest-a-paper-or-correction">Suggest a paper</a>
</p>

The survey examines how AI systems supply learning experience, evaluate outputs, and revise models or agent workflows. It traces cases where the improver itself changes and asks what evidence shows that it improves another AI system more effectively in later rounds.

<!-- BEGIN PAPER CATALOG -->

## Papers

**195 papers** · 108 with code

| Browse by survey role | Papers |
| --- | ---: |
| [Training experience](#training-experience) | 28 |
| [Evaluation feedback](#evaluation-feedback) | 16 |
| [System changes](#system-changes) | 32 |
| [Retained improvement](#retained-improvement) | 22 |
| [Related work and evidence](#related-work-and-evidence) | 91 |
| [Boundary cases](#boundary-cases) | 6 |

### Training experience

<details>
<summary>Show 28 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [AP2O-Coder: Adaptively Progressive Preference Optimization for Reducing Compilation and Runtime Errors in LLM-Generated Code](https://doi.org/10.1609/aaai.v40i41.40771) | AAAI 2026 | Main + supplement | [Code](https://github.com/TsingZ0/AP2O) |
| [GUI0: Self-Evolving Foundational GUI Agents in Super App Ecosystems](https://aclanthology.org/2026.acl-long.2052/) | ACL 2026 | Main + supplement |  |
| [Achieving Expert-Level Agent from Foundation Model via Complexity Curriculum Reinforcement Learning with Synthetic Data](https://openreview.net/forum?id=1sffPGGQyT) | ICLR 2026 | Main + supplement |  |
| [ExGRPO: Learning to Reason from Prior Successes](https://openreview.net/forum?id=701tjQXWVk) | ICLR 2026 | Main + supplement | [Code](https://github.com/ElliottYan/LUFFY/tree/main/ExGRPO) |
| [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://openreview.net/forum?id=j4C0nALrgK) | ICLR 2026 | Main + supplement | [Code](https://github.com/Goedel-LM/Goedel-Prover-V2) |
| [SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning](https://openreview.net/forum?id=7Yayy5fNLg) | ICLR 2026 | Main + supplement | [Code](https://github.com/spiral-rl/spiral) |
| [AdvEvo-MARL: Shaping Internalized Safety through Adversarial Co-Evolution in Multi-Agent Reinforcement Learning](https://openreview.net/forum?id=5D3ZblXmW2) | ICML 2026 | Main + supplement |  |
| [Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs](https://openreview.net/forum?id=sfi4R7lsIP) | ICML 2026 | Supplement | [Code](https://github.com/Easonnoway/TSP) |
| [S^3cMath: Spontaneous Step-Level Self-Correction Makes Large Language Models Better Mathematical Reasoners](https://doi.org/10.1609/aaai.v39i24.34749) | AAAI 2025 | Supplement |  |
| [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://aclanthology.org/2025.acl-long.1336/) | ACL 2025 | Main + supplement | [Code](https://github.com/MinorJerry/OpenWebVoyager) |
| [STEP: Enhancing Video-LLMs' Compositional Reasoning by Spatio-Temporal Graph-guided Self-Training](https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_STEP_Enhancing_Video-LLMs_Compositional_Reasoning_by_Spatio-Temporal_Graph-guided_Self-Training_CVPR_2025_paper.html) | CVPR 2025 | Main + supplement |  |
| [EvolveSearch: An Iterative Self-Evolving Search Agent](https://aclanthology.org/2025.emnlp-main.663/) | EMNLP 2025 | Supplement |  |
| [Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning](https://aclanthology.org/2025.findings-emnlp.629/) | Findings of EMNLP 2025 | Main + supplement |  |
| [Towards Efficient CoT Distillation: Self-Guided Rationale Selector for Better Performance with Fewer Rationales](https://aclanthology.org/2025.findings-emnlp.413/) | Findings of EMNLP 2025 | Supplement | [Code](https://github.com/Leon221220/MoRSD) |
| [SOLID: Self-seeding and Multi-intent Self-instructing LLMs for Generating Intent-aware Information-Seeking Dialogs](https://aclanthology.org/2025.findings-naacl.357/) | Findings of NAACL 2025 | Main + supplement |  |
| [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://openreview.net/forum?id=z4IG090qt2) | ICML 2025 | Main + supplement | [Code](https://github.com/flowersteam/SOAR) |
| [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://openreview.net/forum?id=zWArMedNuW) | ICML 2025 | Main + supplement | [Code](https://github.com/kfdong/STP) |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://openreview.net/forum?id=neZSGqhxDa) | NeurIPS 2025 | Main + supplement |  |
| [Self-Guided Hierarchical Exploration for Generalist Foundation Model Web Agents](https://openreview.net/forum?id=9twwDW60Bw) | NeurIPS 2025 | Main + supplement |  |
| [UICoder: Finetuning Large Language Models to Generate User Interface Code through Automated Feedback](https://aclanthology.org/2024.naacl-long.417/) | ACL 2024 | Main + supplement |  |
| [AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation](https://aclanthology.org/2024.emnlp-main.66/) | EMNLP 2024 | Supplement | [Code](https://github.com/ChiYeungLaw/AMR-Evol) |
| [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://aclanthology.org/2024.findings-emnlp.964/) | Findings of EMNLP 2024 | Supplement |  |
| [Enhancing Alignment using Curriculum Learning & Ranked Preferences](https://aclanthology.org/2024.findings-emnlp.754/) | Findings of EMNLP 2024 | Supplement |  |
| [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://openreview.net/forum?id=CfXh93NDgH) | ICLR 2024 | Main + supplement |  |
| [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://aclanthology.org/2023.acl-long.754/) | ACL 2023 | Main + supplement | [Code](https://github.com/yizhongw/self-instruct) |
| [Active Instruction Tuning: Improving Cross-Task Generalization by Training on Prompt Sensitive Tasks](https://aclanthology.org/2023.emnlp-main.112/) | EMNLP 2023 | Main + supplement | [Code](https://github.com/PlusLabNLP/Active-IT) |
| [Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision](http://papers.nips.cc/paper_files/paper/2023/hash/0764db1151b936aca59249e2c1386101-Abstract-Conference.html) | NeurIPS 2023 | Main + supplement |  |
| [STaR: Bootstrapping Reasoning With Reasoning](https://openreview.net/forum?id=_3ELRdg2sgI) | NeurIPS 2022 | Main + supplement | [Code](https://github.com/ezelikman/STaR) |

</details>

[Back to paper index](#papers)

### Evaluation feedback

<details>
<summary>Show 16 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [Uncertainty-Based Methods for Automated Process Reward Data Construction and Output Aggregation in Mathematical Reasoning](https://doi.org/10.1609/aaai.v40i37.40351) | AAAI 2026 | Supplement | [Code](https://github.com/Jiuzhouh/UnPRM) |
| [AgentV-RL: Scaling Reward Modeling with Agentic Verifier](https://aclanthology.org/2026.findings-acl.1156/) | Findings of ACL 2026 | Supplement | [Code](https://github.com/JiazhengZhang/AgentV-RL) |
| [VITA: Zero-Shot Value Functions via Test-Time Adaptation of Vision–Language Models](https://openreview.net/forum?id=V35oo1SVGH) | ICLR 2026 | Supplement |  |
| [DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research](https://openreview.net/forum?id=97NEP1pyS3) | ICML 2026 | Main + supplement | [Code](https://github.com/rlresearch/dr-tulu) |
| [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://openreview.net/forum?id=TFhUQ6uFCP) | ICML 2026 | Main + supplement |  |
| [Efficient Language-instructed Skill Acquisition via Reward-Policy Co-Evolution](https://doi.org/10.1609/aaai.v39i14.33597) | AAAI 2025 | Main + supplement |  |
| [Boosting Policy and Process Reward Models with Monte Carlo Tree Search in Open-Domain QA](https://aclanthology.org/2025.findings-acl.388/) | Findings of ACL 2025 | Supplement |  |
| [REvolve: Reward Evolution with Large Language Models using Human Feedback](https://openreview.net/forum?id=cJPUpL8mOw) | ICLR 2025 | Main + supplement | [Code](https://github.com/RishiHazra/Revolve) |
| [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://openreview.net/forum?id=A6Y7AqlzLW) | ICLR 2025 | Main + supplement |  |
| [Teaching Language Models to Critique via Reinforcement Learning](https://openreview.net/forum?id=UVoxPlv5E1) | ICML 2025 | Main + supplement | [Code](https://github.com/HKUNLP/critic-rl) |
| [The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement](https://openreview.net/forum?id=D88yhLFzDR) | NeurIPS 2025 | Main + supplement | [Code](https://github.com/rhyang2021/CGI) |
| [SeRTS: Self-Rewarding Tree Search for Biomedical Retrieval-Augmented Generation](https://aclanthology.org/2024.findings-emnlp.71/) | Findings of EMNLP 2024 | Supplement |  |
| [Eureka: Human-Level Reward Design via Coding Large Language Models](https://openreview.net/forum?id=IEduRUO55F) | ICLR 2024 | Main + supplement |  |
| [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://openreview.net/forum?id=hSyW5go0v8) | ICLR 2024 | Main + supplement |  |
| [Self-Rewarding Language Models](https://proceedings.mlr.press/v235/yuan24d.html) | ICML 2024 | Main + supplement |  |
| [Calibrated Self-Rewarding Vision Language Models](https://openreview.net/forum?id=nXYedmTf1T) | NeurIPS 2024 | Main + supplement | [Code](https://github.com/YiyangZhou/CSR) |

</details>

[Back to paper index](#papers)

### System changes

<details>
<summary>Show 32 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [Adaptive Prompt Structure Factorization: A Framework for Self-Discovering and Optimizing Compositional Prompt Programs](https://aclanthology.org/2026.acl-long.537/) | ACL 2026 | Supplement | [Code](https://github.com/T-Lab-CUHKSZ/aPSF) |
| [META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.pdf) | CVPR 2026 | Supplement |  |
| [RAAS: LLM Agentic System Architecture Search with GRPO](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_RAAS_LLM_Agentic_System_Architecture_Search_with_GRPO_CVPR_2026_paper.pdf) | CVPR 2026 | Main + supplement | [Code](https://github.com/ridlog/raas) |
| [Learning from Contrastive Prompts: An Automated Prompt Optimization Framework](https://aclanthology.org/2026.findings-acl.9/) | Findings of ACL 2026 | Supplement |  |
| [MedDCR: Learning to Design Agentic Workflows for Medical Coding](https://aclanthology.org/2026.findings-acl.627/) | Findings of ACL 2026 | Supplement |  |
| [ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents](https://aclanthology.org/2026.findings-acl.931/) | Findings of ACL 2026 | Supplement |  |
| [Can Language Models Discover Scaling Laws?](https://openreview.net/forum?id=TPTtWC0pGk) | ICLR 2026 | Supplement | [Code](https://github.com/linhaowei1/SLD) |
| [Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning](https://openreview.net/forum?id=XCW1l9qcxy) | ICLR 2026 | Supplement | [Code](https://github.com/transductive-visualprogram/tvp) |
| [TusoAI: Agentic Optimization for Scientific Methods](https://openreview.net/forum?id=0M6BfcAVMW) | ICLR 2026 | Main + supplement | [Code](https://github.com/Alistair-Turcan/TusoAI) |
| [EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows](https://openreview.net/forum?id=cdWnpXkcQo) | ICML 2026 | Main + supplement |  |
| [Dolphin: Moving Towards Closed-loop Auto-research through Thinking, Practice, and Feedback](https://aclanthology.org/2025.acl-long.1056/) | ACL 2025 | Main + supplement | [Code](https://github.com/Alpha-Innovator/Dolphin) |
| [EvoVLMA: Evolutionary Vision-Language Model Adaptation](http://dx.doi.org/10.1145/3746027.3755520) | ACM MM 2025 | Main + supplement | [Code](https://github.com/kding1225/EvoVLMA) |
| [NADER: Neural Architecture Design via Multi-Agent Collaboration](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_NADER_Neural_Architecture_Design_via_Multi-Agent_Collaboration_CVPR_2025_paper.html) | CVPR 2025 | Main + supplement |  |
| [Automated Design of Agentic Systems](https://openreview.net/forum?id=t9U3LW7JVX) | ICLR 2025 | Main + supplement | [Code](https://github.com/ShengranHu/ADAS) |
| [Pareto Prompt Optimization](https://openreview.net/forum?id=HGCk5aaSvE) | ICLR 2025 | Supplement | [Code](https://github.com/guangzhao27/ParetoPrompt) |
| [Adaptive Self-improvement LLM Agentic System for ML Library Development](https://openreview.net/forum?id=gdsZ3uMPsY) | ICML 2025 | Supplement | [Code](https://github.com/zhang677/PCL-lite) |
| [FunBO: Discovering Acquisition Functions for Bayesian Optimization with FunSearch](https://openreview.net/forum?id=XjbJR9374o) | ICML 2025 | Main + supplement |  |
| [RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy](https://openreview.net/forum?id=9UExQpH078) | ICML 2025 | Main + supplement | [Code](https://github.com/PasaLab/RZ-NAS) |
| [Optimizing generative AI by backpropagating language model feedback](https://doi.org/10.1038/s41586-025-08661-4) | Nature 2025 | Main + supplement |  |
| [Language Modeling by Language Models](https://openreview.net/forum?id=VrCdsZBbIg) | NeurIPS 2025 | Main + supplement | [Code](https://github.com/allenai/genesys) |
| [Empowering Large Language Model Agents through Action Learning](https://openreview.net/forum?id=KqK5XcgEhR) | COLM 2024 | Supplement |  |
| [CLOVA: A Closed-LOop Visual Assistant with Tool Usage and Update](https://openaccess.thecvf.com/content/CVPR2024/html/Gao_CLOVA_A_Closed-LOop_Visual_Assistant_with_Tool_Usage_and_Update_CVPR_2024_paper.html) | CVPR 2024 | Main + supplement | [Code](https://github.com/clova-tool/CLOVA-tool) |
| [Language Models as Black-Box Optimizers for Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Language_Models_as_Black-Box_Optimizers_for_Vision-Language_Models_CVPR_2024_paper.html) | CVPR 2024 | Supplement |  |
| [Dynamic Rewarding with Prompt Optimization Enables Tuning-free Self-Alignment of Language Models](https://aclanthology.org/2024.emnlp-main.1220/) | EMNLP 2024 | Supplement | [Code](https://github.com/Singla17/DRPO) |
| [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://openreview.net/forum?id=ZG3RaNIsO8) | ICLR 2024 | Main + supplement | [Code](https://github.com/beeevita/EvoPrompt) |
| [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://openreview.net/forum?id=sY5N0zY5Od) | ICLR 2024 | Main + supplement |  |
| [Large Language Models as Optimizers](https://openreview.net/forum?id=Bb4VGOWELI) | ICLR 2024 | Main + supplement | [Code](https://github.com/google-deepmind/opro) |
| [tnGPS: Discovering Unknown Tensor Network Structure Search Algorithms via Large Language Models (LLMs)](https://proceedings.mlr.press/v235/zeng24b.html) | ICML 2024 | Main + supplement | [Code](https://github.com/ChaoLiAtRIKEN/tngps) |
| [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://openreview.net/forum?id=UkxJd64mki) | NeurIPS 2024 | Supplement | [Code](https://github.com/gao-xiao-bai/StrategyLLM) |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://openreview.net/forum?id=ehfRiF0R3a) | TMLR 2024 | Main + supplement |  |
| [Universal Self-Adaptive Prompting](https://aclanthology.org/2023.emnlp-main.461/) | EMNLP 2023 | Supplement |  |
| [Large Language Models are Human-Level Prompt Engineers](https://openreview.net/forum?id=92gvk82DE-) | ICLR 2023 | Supplement | [Code](https://github.com/keirp/automatic_prompt_engineer) |

</details>

[Back to paper index](#papers)

### Retained improvement

<details>
<summary>Show 22 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [From Failure to Feedback: Group Revision Unlocks Hard Cases in Object-Level Grounding](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_From_Failure_to_Feedback_Group_Revision_Unlocks_Hard_Cases_in_CVPR_2026_paper.pdf) | CVPR 2026 | Supplement |  |
| [Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation](https://aclanthology.org/2026.findings-acl.719/) | Findings of ACL 2026 | Main + supplement | [Code](https://github.com/Bairong-Xdynamics/MistakeNotebookLearning) |
| [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://openreview.net/forum?id=pUpzQZTvGY) | ICLR 2026 | Main + supplement |  |
| [Group Verification-based Policy Optimization for Interactive Coding Agents](https://openreview.net/forum?id=RY47Tq0VsV) | ICLR 2026 | Supplement |  |
| [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://openreview.net/forum?id=T0EiEuhOOL) | ICLR 2026 | Main + supplement | [Code](https://github.com/metauto-ai/HGM) |
| [From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory](https://openreview.net/forum?id=gNWNtstp3r) | ICML 2026 | Main + supplement | [Code](https://github.com/walkeralan123/MemoPilot) |
| [Post-Training LLMs as Better Decision-Making Agents: A Regret-Minimization Approach](https://openreview.net/forum?id=dclUuUHjrA) | ICML 2026 | Supplement |  |
| [Contextual Experience Replay for Self-Improvement of Language Agents](https://aclanthology.org/2025.acl-long.694/) | ACL 2025 | Main + supplement |  |
| [SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection](https://aclanthology.org/2025.emnlp-main.839/) | EMNLP 2025 | Main + supplement |  |
| [Self-Correcting Code Generation Using Small Language Models](https://aclanthology.org/2025.findings-emnlp.127/) | Findings of EMNLP 2025 | Main + supplement | [Code](https://github.com/jeonghun3572/CoCoS) |
| [GTR: Guided Thought Reinforcement Prevents Thought Collapse in RL-based VLM Agent Training](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_GTR_Guided_Thought_Reinforcement_Prevents_Thought_Collapse_in_RL-based_VLM_ICCV_2025_paper.html) | ICCV 2025 | Main + supplement |  |
| [Afterburner: Reinforcement Learning Facilitates Self-Improving Code Efficiency Optimization](https://openreview.net/forum?id=At8OUlyTOu) | NeurIPS 2025 | Supplement | [Code](https://github.com/Elfsong/Afterburner) |
| [metaTextGrad: Automatically optimizing language model optimizers](https://openreview.net/forum?id=10s01YrlKp) | NeurIPS 2025 | Main + supplement |  |
| [VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning](https://openreview.net/forum?id=4oYxzssbVg) | NeurIPS 2025 | Supplement | [Code](https://github.com/TIGER-AI-Lab/VL-Rethinker) |
| [ExpeL: LLM Agents Are Experiential Learners](https://doi.org/10.1609/aaai.v38i17.29936) | AAAI 2024 | Main + supplement | [Code](https://github.com/LeapLabTHU/ExpeL) |
| [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://aclanthology.org/2024.acl-long.292/) | ACL 2024 | Supplement | [Code](https://github.com/zwq2018/Agent-Pro) |
| [Self-Evolving GPT: A Lifelong Autonomous Experiential Learner](https://aclanthology.org/2024.acl-long.346/) | ACL 2024 | Main + supplement | [Code](https://github.com/ArrogantL/se_gpt) |
| [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://openreview.net/forum?id=46Zgqo4QIU) | COLM 2024 | Main + supplement | [Code](https://github.com/microsoft/stop) |
| [Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution](https://proceedings.mlr.press/v235/fernando24a.html) | ICML 2024 | Main + supplement |  |
| [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://openreview.net/forum?id=DRC9pZwBwR) | NeurIPS 2024 | Main + supplement | [Code](https://github.com/cmu-mind/RISE) |
| [Large Language Models can Implement Policy Iteration](https://openreview.net/forum?id=LWxjWoBTsr) | NeurIPS 2023 | Supplement | [Code](https://github.com/ethanabrooks/icpi) |
| [Reflexion: language agents with verbal reinforcement learning](https://openreview.net/forum?id=vAElhFcKW6) | NeurIPS 2023 | Main + supplement | [Code](https://github.com/noahshinn024/reflexion) |

</details>

[Back to paper index](#papers)

### Related work and evidence

<details>
<summary>Show 91 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [Evolving Generalist Virtual Agents with Generative and Associative Memory](https://doi.org/10.1609/aaai.v40i15.38300) | AAAI 2026 | Main |  |
| [Counteracting the Matthew Effect in Self-Improvement of LVLMs through Head-Tail Re-balancing](https://aclanthology.org/2026.acl-long.1010/) | ACL 2026 | Main | [Code](https://github.com/XinGuo2002/Head-Tail-Rebalancing) |
| [SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks](https://aclanthology.org/2026.acl-long.926/) | ACL 2026 | Main |  |
| [The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination](https://aclanthology.org/2026.acl-long.376/) | ACL 2026 | Main | [Code](https://github.com/albert-y1n/Reasoning_Trap) |
| [Enhancing Jailbreak Attacks on LLMs via Persona Prompts](https://arxiv.org/abs/2507.22171) | arXiv 2026 | Main | [Code](https://github.com/CjangCjengh/Generic_Persona) |
| [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | arXiv 2026 | Main |  |
| [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314) | arXiv 2026 | Main |  |
| [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | arXiv 2026 | Main + supplement |  |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | arXiv 2026 | Main |  |
| [Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification](https://aclanthology.org/2026.findings-acl.1243/) | Findings of ACL 2026 | Main | [Code 1](https://github.com/yxwan123/DeepVerifier) · [Code 2](https://github.com/Tencent/CognitiveKernel-Pro) |
| [Credit-Budgeted ICPC-Style Coding: When LLM Agents Must Pay for Every Decision](https://openreview.net/forum?id=WC2g3zDF2o) | ICLR 2026 | Main | [Code](https://github.com/maple-zhou/USACOArena) |
| [EVALUATING MEMORY IN LLM AGENTS VIA INCRE- MENTAL MULTI-TURN INTERACTIONS](https://openreview.net/forum?id=DT7JyQC3MR) | ICLR 2026 | Main | [Code](https://github.com/HUST-AI-HYZ/MemoryAgentBench) |
| [Forget Forgetting: Continual Learning in a World of Abundant Memory](https://openreview.net/forum?id=fvL8IIEPxG) | ICLR 2026 | Main |  |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://openreview.net/forum?id=RQm2KQTM5r) | ICLR 2026 | Main | [Code](https://github.com/gepa-ai/gepa) |
| [WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality](https://openreview.net/forum?id=CCSPm6V5EF) | ICLR 2026 | Main | [Code](https://github.com/lcy2723/WebDevJudge) |
| [Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents](https://openreview.net/forum?id=Fd1jgQQW28) | ICLR 2026 | Main | [Code](https://github.com/ShaoShuai0605/Misevolution) |
| [Alignment Risks from Capability-Seeking RL Training](https://openreview.net/forum?id=Rbeke9PVvD) | ICML 2026 | Main | [Code](https://github.com/YujunZhou/Capability-seeking-RL-risk) |
| [Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences](https://openreview.net/forum?id=kwvtSA9ed3) | ICML 2026 | Main |  |
| [Depth over Fidelity in Fixed-Budget Noisy Evolution Strategies](https://openreview.net/forum?id=woocESr6ga) | ICML 2026 | Main | [Code](https://github.com/sichen-wang/Depth-over-Fidelity_ICML2026) |
| [Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math](https://openreview.net/forum?id=Dkwqzk5sAD) | ICML 2026 | Main |  |
| [Learning to Discover at Test Time](https://openreview.net/forum?id=96zNuQrH9Y) | ICML 2026 | Main | [Code](https://github.com/test-time-training/discover) |
| [Multi-Objective Preference Optimization: Improving Human Alignment of Generative Models](https://openreview.net/forum?id=AFqHVyanzY) | ICML 2026 | Main |  |
| [Position: ICML Should Treat Hosted LLM APIs as Versioned Dependencies and Require Drift-Audit Artifacts](https://openreview.net/forum?id=ivW5cQd53r) | ICML 2026 | Main |  |
| [Position: Modular Memory is the Key to Continual Learning Agents](https://openreview.net/forum?id=iBXcqA5N6j) | ICML 2026 | Main |  |
| [Scaling Small Agents Through Strategy Auctions](https://openreview.net/forum?id=elXuA5wTWV) | ICML 2026 | Main | [Code](https://github.com/facebookresearch/hst-bench) |
| [Structurally Aligned Subtask-Level Memory for Software Engineering Agents](https://openreview.net/forum?id=2CoRS45Ucj) | ICML 2026 | Main |  |
| [VeRO: A Harness for Agents to Optimize Agents](https://openreview.net/forum?id=zQzmwG2Nue) | ICML 2026 | Main | [Code](https://github.com/scaleapi/vero) |
| [AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems](https://www.preprints.org/manuscript/202608.2108) | Preprint 2026 | Main + supplement |  |
| [Diving into Reliable Self-Evolving Agents: A Survey](https://openreview.net/forum?id=CGO1hDTHNe) | Preprint 2026 | Main + supplement | [Code](https://github.com/wkqdzkd/Awesome-Reliable-Self-Evolving-Agents) |
| [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://openreview.net/forum?id=CTr3bovS5F) | TMLR 2026 | Main | [Code](https://github.com/CharlesQ9/Self-Evolving-Agents) |
| [MultiMind: Enhancing Werewolf Agents with Multimodal Reasoning and Theory of Mind](http://dx.doi.org/10.1145/3746027.3755752) | ACM MM 2025 | Main | [Code](https://github.com/CjangCjengh/onuw) |
| [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407) | arXiv 2025 | Main + supplement |  |
| [Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning](https://openreview.net/forum?id=dNW3RGW0gi) | COLM 2025 | Main | [Code](https://github.com/CLAIRE-Labo/EvoTune) |
| [Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Can_Large_Vision-Language_Models_Correct_Semantic_Grounding_Errors_By_Themselves_CVPR_2025_paper.html) | CVPR 2025 | Main |  |
| [Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation](https://aclanthology.org/2025.emnlp-main.1182/) | EMNLP 2025 | Main | [Code](https://github.com/DongryeolLee96/FRAME) |
| [Local Look-Ahead Guidance via Verifier-in-the-Loop for Automated Theorem Proving](https://aclanthology.org/2025.findings-acl.825/) | Findings of ACL 2025 | Main |  |
| [Inefficiencies of Meta Agents for Agent Design](https://aclanthology.org/2025.findings-emnlp.1135/) | Findings of EMNLP 2025 | Main | [Code](https://github.com/batu-el/meta-agent-inefficiency) |
| [DVM: Towards Controllable LLM Agents in Social Deduction Games](http://dx.doi.org/10.1109/ICASSP49660.2025.10888525) | ICASSP 2025 | Main |  |
| [AFlow: Automating Agentic Workflow Generation](https://openreview.net/forum?id=z5uVAKwmjf) | ICLR 2025 | Main | [Code](https://github.com/FoundationAgents/AFlow) |
| [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://openreview.net/forum?id=V4y0CpX4hK) | ICLR 2025 | Main | [Code](https://github.com/agiresearch/ASB) |
| [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://openreview.net/forum?id=Uo4EHT4ZZ8) | ICLR 2025 | Main | [Code](https://github.com/lean-dojo/LeanAgent) |
| [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://openreview.net/forum?id=chfJJYC3iL) | ICLR 2025 | Main |  |
| [MLE-Bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://openreview.net/forum?id=6s5uXNWGIh) | ICLR 2025 | Main | [Code](https://github.com/openai/mle-bench) |
| [RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code](https://openreview.net/forum?id=NiNIthntx7) | ICLR 2025 | Main | [Code](https://github.com/microsoft/RefactorBench) |
| [Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?](https://openreview.net/forum?id=Cnwz9jONi5) | ICLR 2025 | Main |  |
| [Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment](https://openreview.net/forum?id=QnjfkhrbYK) | ICML 2025 | Main |  |
| [MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://openreview.net/forum?id=fyi34BxCwq) | ICML 2025 | Main | [Code](https://github.com/google-deepmind/mona) |
| [Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges](https://openreview.net/forum?id=ZtX0MBT6mf) | ICML 2025 | Main |  |
| [Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning](https://openreview.net/forum?id=vTWNVYuvuF) | NeurIPS 2025 | Main | [Code](https://github.com/sparkle-reasoning/sparkle) |
| [Learning Interestingness in Automated Mathematical Theory Formation](https://openreview.net/forum?id=RespmwOoCH) | NeurIPS 2025 | Main | [Code](https://github.com/trishullab/Fermat) |
| [Self-Verifying Reflection Helps Transformers with CoT Reasoning](https://openreview.net/forum?id=4MvqmXnCEr) | NeurIPS 2025 | Main | [Code](https://github.com/zwyu-ai/self-verifying-reflection-reasoning) |
| [Spend Wisely: Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping](https://openreview.net/forum?id=aqpHTPC63N) | NeurIPS 2025 | Main | [Code](https://github.com/zylipku/spend-wisely) |
| [Can LLMs Learn from Previous Mistakes? Investigating LLMs’ Errors to Boost for Reasoning](https://aclanthology.org/2024.acl-long.169/) | ACL 2024 | Main | [Code](https://github.com/YookiTong/Learn-from-Mistakes-CotErrorSet) |
| [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) | arXiv 2024 | Main + supplement |  |
| [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations](https://openreview.net/forum?id=BAakY1hNKS) | COLM 2024 | Main | [Code](https://github.com/microsoft/autogen) |
| [Evaluating LLMs at Detecting Errors in LLM Responses](https://openreview.net/forum?id=dnwRScljXr) | COLM 2024 | Main | [Code](https://github.com/psunlpgroup/ReaLMistake) |
| [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://openreview.net/forum?id=oRXPiSOGH9) | COLM 2024 | Main |  |
| [Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Embodied_Multi-Modal_Agent_trained_by_an_LLM_from_a_Parallel_CVPR_2024_paper.html) | CVPR 2024 | Main | [Code](https://github.com/stevenyangyj/Emma-Alfworld) |
| [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://openreview.net/forum?id=y4vaskUK1b) | ECCV 2024 Workshop The Dark Side of Generative AIs and Beyond 2024 | Main |  |
| [Humans or LLMs as the Judge? A Study on Judgement Bias](https://aclanthology.org/2024.emnlp-main.474/) | EMNLP 2024 | Main | [Code](https://github.com/FreedomIntelligence/Humans_LLMs_Judgement_Bias) |
| [LLM-Based Agent Society Investigation: Collaboration and Confrontation in Avalon Gameplay](https://aclanthology.org/2024.emnlp-main.7/) | EMNLP 2024 | Main | [Code](https://github.com/3DAgentWorld/LLM-Game-Agent) |
| [DebugBench: Evaluating Debugging Capability of Large Language Models](https://aclanthology.org/2024.findings-acl.247/) | Findings of ACL 2024 | Main | [Code](https://github.com/thunlp/DebugBench) |
| [RAG-Studio: Towards In-Domain Adaptation of Retrieval Augmented Generation Through Self-Alignment](https://aclanthology.org/2024.findings-emnlp.41/) | Findings of EMNLP 2024 | Main | [Code](https://github.com/kyriemao/rag_studio) |
| [Is Self-Repair a Silver Bullet for Code Generation?](https://openreview.net/forum?id=y0GJXRungR) | ICLR 2024 | Main | [Code](https://github.com/theoxo/self-repair) |
| [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://openreview.net/forum?id=VtmBAGCN7o) | ICLR 2024 | Main | [Code](https://github.com/geekan/MetaGPT) |
| [SWE-bench: Can Language Models Resolve Real-world Github Issues?](https://proceedings.iclr.cc/paper_files/paper/2024/file/edac78c3e300629acfe6cbe9ca88fb84-Paper-Conference.pdf) | ICLR 2024 | Main |  |
| [MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://proceedings.mlr.press/v235/huang24y.html) | ICML 2024 | Main | [Code](https://github.com/snap-stanford/MLAgentBench) |
| [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://openreview.net/forum?id=uydQ2W41KO) | ICML 2024 | Main |  |
| [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://proceedings.mlr.press/v235/chen24j.html) | ICML 2024 | Main | [Code](https://github.com/uclaml/SPIN) |
| [Towards Theoretical Understandings of Self-Consuming Generative Models](https://proceedings.mlr.press/v235/fu24i.html) | ICML 2024 | Main |  |
| [AI models collapse when trained on recursively generated data](https://doi.org/10.1038/s41586-024-07566-y) | Nature 2024 | Main |  |
| [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://openreview.net/forum?id=evP9mxNNxJ) | NeurIPS 2024 | Main | [Code](https://github.com/MMStar-Benchmark/MMStar) |
| [Code Repair with LLMs gives an Exploration-Exploitation Tradeoff](https://openreview.net/forum?id=o863gX6DxA) | NeurIPS 2024 | Main |  |
| [Learning Formal Mathematics From Intrinsic Motivation](https://openreview.net/forum?id=uNKlTQ8mBD) | NeurIPS 2024 | Main | [Code](https://github.com/gpoesia/minimo) |
| [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](http://papers.nips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html) | NeurIPS 2024 | Main |  |
| [Automatic Prompt Optimization with \`\`Gradient Descent'' and Beam Search](https://aclanthology.org/2023.emnlp-main.494/) | EMNLP 2023 | Main | [Code](https://github.com/microsoft/LMOps/tree/main/prompt_optimization) |
| [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://aclanthology.org/2023.findings-acl.507/) | Findings of ACL 2023 | Main | [Code](https://github.com/google-research/distilling-step-by-step) |
| [A Closer Look into Using Large Language Models for Automatic Evaluation](https://aclanthology.org/2023.findings-emnlp.599/) | Findings of EMNLP 2023 | Main | [Code](https://github.com/d223302/A-Closer-Look-To-LLM-Evaluation) |
| [GPT-4 as an Effective Zero-Shot Evaluator for Scientific Figure Captions](https://aclanthology.org/2023.findings-emnlp.363/) | Findings of EMNLP 2023 | Main | [Code](https://github.com/Crowd-AI-Lab/SciCap-Eval) |
| [Large Language Models are Not Yet Human-Level Evaluators for Abstractive Summarization](https://aclanthology.org/2023.findings-emnlp.278/) | Findings of EMNLP 2023 | Main | [Code](https://github.com/DAMO-NLP-SG/LLM_summeval) |
| [A Theory of Dynamic Benchmarks](https://openreview.net/forum?id=i8L9qoeZOS) | ICLR 2023 | Main |  |
| [Language Models Can Teach Themselves to Program Better](https://openreview.net/forum?id=SaRj2ka1XZ3) | ICLR 2023 | Main | [Code](https://github.com/microsoft/PythonProgrammingPuzzles) |
| [Scaling Laws for Reward Model Overoptimization](https://proceedings.mlr.press/v202/gao23h.html) | ICML 2023 | Main |  |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://proceedings.neurips.cc/paper_files/paper/2023/file/a85b405ed65c6477a4fe8302b5e06ce7-Paper-Conference.pdf) | NeurIPS 2023 | Main |  |
| [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](http://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html) | NeurIPS 2023 | Main |  |
| [LIMA: Less Is More for Alignment](https://openreview.net/forum?id=KBMOKmX2he) | NeurIPS 2023 | Main |  |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](http://papers.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) | NeurIPS 2023 | Main |  |
| [On the Limitations of Reference-Free Evaluations of Generated Text](https://aclanthology.org/2022.emnlp-main.753/) | EMNLP 2022 | Main |  |
| [Learning to repair: Repairing model output errors after deployment using a dynamic memory of feedback](https://aclanthology.org/2022.findings-naacl.26/) | Findings of NAACL 2022 | Main | [Code](https://github.com/allenai/interscript) |
| [Autoformalization with Large Language Models](https://openreview.net/forum?id=IUikebJ1Bf0) | NeurIPS 2022 | Main |  |
| [Training language models to follow instructions with human feedback](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf) | NeurIPS 2022 | Main |  |

</details>

[Back to paper index](#papers)

### Boundary cases

<details>
<summary>Show 6 papers</summary>

| Paper | Venue | Corpus | Code |
| --- | --- | --- | --- |
| [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://openreview.net/forum?id=ArifAHrEVD) | ICML 2025 | Supplement | [Code](https://github.com/yafuly/TPO) |
| [SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents](https://openreview.net/forum?id=isATAFP71B) | NeurIPS 2025 | Supplement | [Code](https://github.com/JARVIS-Xs/SE-Agent) |
| [QueryAgent: A Reliable and Efficient Reasoning Framework with Environmental Feedback based Self-Correction](https://aclanthology.org/2024.acl-long.274/) | ACL 2024 | Supplement | [Code](https://github.com/cdhx/QueryAgent) |
| [Large Language Models Can Self-Correct with Key Condition Verification](https://aclanthology.org/2024.emnlp-main.714/) | EMNLP 2024 | Supplement | [Code](https://github.com/wzy6642/ProCo) |
| [Teaching Large Language Models to Self-Debug](https://openreview.net/forum?id=KuPixIqPiq) | ICLR 2024 | Main + supplement |  |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://openreview.net/forum?id=S37hOerQLB) | NeurIPS 2023 | Main + supplement | [Code](https://github.com/madaan/self-refine) |

</details>

[Back to paper index](#papers)

<!-- END PAPER CATALOG -->

### Suggest a paper or correction

Open an [issue](https://github.com/3DAgentWorld/awesome-ai-for-ai/issues/new) with the title, DOI or arXiv link, the relevant survey role, and a sentence explaining the connection. Include the official code link when available.

After updating `js/papers-data.js`, run `python scripts/render_paper_catalog.py` to refresh the README tables.

## Citation

[Download BibTeX](citation.bib)

```bibtex
@article{202609.0591,
  title   = {A Survey on {AI} for {AI}: When the Improver Becomes the Improvee},
  author  = {Ye, Deheng and Zhang, Zheng and Wang, Hao and Miao, Chunyan},
  journal = {Preprints.org},
  year    = {2026},
  doi     = {10.20944/preprints202609.0591.v2},
  url     = {https://doi.org/10.20944/preprints202609.0591.v2}
}
```

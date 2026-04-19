"""把示例内容整理成固定格式的“今日同步卡”。"""

from __future__ import annotations


def build_today_sync_card(raw_text: str) -> str:
    """根据原始文本生成演示版同步卡。

    这是最小演示版：
    - 不做复杂 NLP 分类
    - 只按固定结构输出，内容用简单规则提取
    """
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    today_new = "；".join(lines[:3]) if lines else "（暂无）"
    worth_archive = "；".join([line for line in lines if "灵感" in line or "书" in line][:2]) or "整理为“灵感清单”"
    need_confirm = "；".join([line for line in lines if "确认" in line or "检查" in line][:2]) or "（暂无需要确认）"

    summary = (
        "今天主要记录了生活灵感与待办提醒，"
        "适合晚间统一整理，并把可执行事项放进明日计划。"
    )

    card = (
        "# 今日同步卡\n\n"
        f"- 今日新增：{today_new}\n"
        f"- 值得归档：{worth_archive}\n"
        f"- 待确认：{need_confirm}\n"
        f"- 给知言看的摘要：{summary}\n"
    )
    return card

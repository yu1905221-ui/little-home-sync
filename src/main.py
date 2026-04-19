"""最小演示版入口：生成“今日同步卡”到本地文件。"""

from pathlib import Path

from sample_data import SAMPLE_NOTES
from summarize import build_today_sync_card


def main() -> None:
    output_path = Path("output/today_sync.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sync_card = build_today_sync_card(SAMPLE_NOTES)
    output_path.write_text(sync_card, encoding="utf-8")

    print(f"已生成：{output_path}")


if __name__ == "__main__":
    main()

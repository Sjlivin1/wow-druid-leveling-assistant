# druid_assistant.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QProgressBar, QPushButton, QLineEdit
)

class DruidLevelingAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WoW Classic Druid Leveling Assistant (23–60)")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.level_label = QLabel("Select your current level:")
        layout.addWidget(self.level_label)

        self.level_dropdown = QComboBox()
        for i in range(23, 61):
            self.level_dropdown.addItem(str(i))
        self.level_dropdown.currentIndexChanged.connect(self.update_zone_recommendation)
        layout.addWidget(self.level_dropdown)

        self.zone_label = QLabel("Recommended Zone: ")
        layout.addWidget(self.zone_label)

        self.talent_label = QLabel("Suggested Spec: Feral (Cat Form for leveling)")
        layout.addWidget(self.talent_label)

        self.milestone_label = QLabel("Next Druid Milestone: Travel Form at 30!")
        layout.addWidget(self.milestone_label)

        self.xp_input = QLineEdit()
        self.xp_input.setPlaceholderText("Enter % XP toward next level (0–100)")
        layout.addWidget(self.xp_input)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.update_xp_btn = QPushButton("Update XP Progress")
        self.update_xp_btn.clicked.connect(self.update_xp_bar)
        layout.addWidget(self.update_xp_btn)

        self.setLayout(layout)
        self.update_zone_recommendation()

    def update_zone_recommendation(self):
        level = int(self.level_dropdown.currentText())
        zone = self.get_zone_by_level(level)
        milestone = self.get_druid_milestone(level)

        self.zone_label.setText(f"Recommended Zone: {zone}")
        self.milestone_label.setText(f"Next Druid Milestone: {milestone}")

    def get_zone_by_level(self, level):
        if 23 <= level <= 27:
            return "Ashenvale or Hillsbrad Foothills"
        elif 28 <= level <= 32:
            return "Stranglethorn Vale (start quests)"
        elif 33 <= level <= 37:
            return "Desolace or Arathi Highlands"
        elif 38 <= level <= 42:
            return "Dustwallow Marsh / Badlands"
        elif 43 <= level <= 47:
            return "Tanaris / Hinterlands"
        elif 48 <= level <= 52:
            return "Un'Goro Crater / Felwood"
        elif 53 <= level <= 56:
            return "Western Plaguelands / Burning Steppes"
        elif 57 <= level <= 60:
            return "Eastern Plaguelands / Winterspring / BRD dungeons"
        else:
            return "Unknown"

    def get_druid_milestone(self, level):
        milestones = {
            30: "Travel Form",
            40: "Mount (40g cost)",
            50: "Moonkin Form (if Balance)",
            58: "Dire Maul Class Quest for idol",
        }
        for key in sorted(milestones.keys()):
            if level < key:
                return milestones[key]
        return "You’re max level! Time to raid."

    def update_xp_bar(self):
        try:
            xp = int(self.xp_input.text())
            xp = max(0, min(100, xp))  # clamp 0–100
            self.progress_bar.setValue(xp)
        except ValueError:
            self.progress_bar.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DruidLevelingAssistant()
    window.show()
    sys.exit(app.exec_())

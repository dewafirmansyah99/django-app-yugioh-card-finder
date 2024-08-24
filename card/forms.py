from django import forms


class TableForm(forms.Form):
    MONSTER = [
        ('', '----'),
        ("Effect Monster", "Effect Monster"),
        ("Flip Effect Monster", "Flip Effect Monster"),
        ("Flip Tuner Effect Monster", "Flip Tuner Effect Monster"),
        ("Gemini Monster", "Gemini Monster"),
        ("Normal Monster", "Normal Monster"),
        ("Normal Tuner Monster", "Normal Tuner Monster"),
        ("Pendulum Effect Monster", "Pendulum Effect Monster"),
        ("Pendulum Effect Ritual Monster", "Pendulum Effect Ritual Monster"),
        ("Pendulum Flip Effect Monster", "Pendulum Flip Effect Monster"),
        ("Pendulum Normal Monster", "Pendulum Normal Monster"),
        ("Pendulum Tuner Effect Monster", "Pendulum Tuner Effect Monster"),
        ("Ritual Effect Monster", "Ritual Effect Monster"),
        ("Ritual Monster", "Ritual Monster"),
        ("Spirit Monster", "Spirit Monster"),
        ("Toon Monster", "Toon Monster"),
        ("Tuner Monster", "Tuner Monster"),
        ("Union Effect Monster", "Union Effect Monster"),
        ("Fusion Monster", "Fusion Monster"),
        ("Link Monster", "Link Monster"),
        ("Pendulum Effect Fusion Monster", "Pendulum Effect Fusion Monster"),
        ("Synchro Monster", "Synchro Monster"),
        ("Synchro Pendulum Effect Monster", "Synchro Pendulum Effect Monster"),
        ("Synchro Tuner Monster", "Synchro Tuner Monster"),
        ("XYZ Monster", "XYZ Monster"),
        ("XYZ Pendulum Effect Monster", "XYZ Pendulum Effect Monster"),
        ("Token", "Token")
    ]

    LEVEL = [
        ('', '----'),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ]

    RACE_MONSTER = [
        ('', '----'),
        ("Aqua", "Aqua"),
        ("Beast", "Beast"),
        ("Beast-Warrior", "Beast-Warrior"),
        ("Creator-God", "Creator-God"),
        ("Cyberse", "Cyberse"),
        ("Dinosaur", "Dinosaur"),
        ("Divine-Beast", "Divine-Beast"),
        ("Dragon", "Dragon"),
        ("Fairy", "Fairy"),
        ("Fiend", "Fiend"),
        ("Fish", "Fish"),
        ("Insect", "Insect"),
        ("Machine", "Machine"),
        ("Plant", "Plant"),
        ("Psychic", "Psychic"),
        ("Pyro", "Pyro"),
        ("Reptile", "Reptile"),
        ("Rock", "Rock"),
        ("Sea Serpent", "Sea Serpent"),
        ("Spellcaster", "Spellcaster"),
        ("Thunder", "Thunder"),
        ("Warrior", "Warrior"),
        ("Winged Beast", "Winged Beast"),
        ("Wyrm", "Wyrm"),
        ("Zombie", "Zombie"),
    ]

    RACE_SPELL = [
        ('', '----'),
        ("Normal", "Normal"),
        ("Field", "Field"),
        ("Equip", "Equip"),
        ("Continuous", "Continuous"),
        ("Quick-Play", "Quick-Play"),
        ("Ritual", "Ritual")
    ]

    RACE_TRAP = [
        ('', '----'),
        ("Normal", "Normal"),
        ("Continuous", "Continuous"),
        ("Counter", "Counter")
    ]
    number = forms.IntegerField(label=True, required=False, widget=forms.NumberInput(attrs={'type': 'number', 'id': 'input_number', 'class': 'form-control me-2', 'placeholder': 'Input Number', 'style': 'display: none; background-color: #C5F0D8; font-family: pixel; -webkit-appearance: none; -moz-appearance: textfield;'}))
    char = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'type': 'char', 'name': 'card_name', 'id': 'input_name', 'class': 'form-control col-xs-2', 'placeholder': 'Input Name', 'style': 'display: none; background-color: #C5F0D8; font-family: pixel;'}))
    monster = forms.ChoiceField(label=False, initial={'': '-------'}, required=False, choices=MONSTER, widget=forms.Select(attrs={'name': 'monster_type', 'id': 'input_monster', 'class': 'form-select col-xs-2', 'placeholder': 'Input Monster', 'style': 'background-color: #C5F0D8; font-family: pixel;'}))
    level = forms.ChoiceField(label=False, initial={'': '-------'}, required=False, choices=LEVEL, widget=forms.Select(attrs={'name': 'card_level', 'id': 'input_level', 'class': 'form-select col-xs-2', 'placeholder': 'Input Level', 'style': 'background-color: #C5F0D8; font-family: pixel;'}))
    race_monster = forms.ChoiceField(label=False, initial={'': '-------'}, required=False, choices=RACE_MONSTER, widget=forms.Select(attrs={'name': 'card_race_monster', 'id': 'input_race_monster', 'class': 'form-select col-xs-2', 'placeholder': 'Input Race', 'style': 'background-color: #C5F0D8; font-family: pixel;'}))
    race_spell = forms.ChoiceField(label=False, initial={'': '-------'}, required=False, choices=RACE_SPELL, widget=forms.Select(attrs={'name': 'card_race_spell', 'id': 'input_race_spell', 'class': 'form-select col-xs-2', 'placeholder': 'Input Race', 'style': 'display: none; background-color: #C5F0D8; font-family: pixel;'}))
    race_trap = forms.ChoiceField(label=False, initial={'': '-------'}, required=False, choices=RACE_TRAP, widget=forms.Select(attrs={'name': 'card_race_trap', 'id': 'input_race_trap', 'class': 'form-select col-xs-2', 'placeholder': 'Input Race', 'style': 'display: none; background-color: #C5F0D8; font-family: pixel;'}))


class ReloadForm(forms.Form):
    char = forms.CharField(label=False, widget=forms.TextInput(attrs={'type': 'char', 'name': 'card_name', 'id': 'input_number', 'class': 'form-control col-xs-2', 'placeholder': 'Input Name'}))

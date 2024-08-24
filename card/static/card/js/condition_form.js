function ChangeMode() {
    let mode = document.getElementById('inputGroupSelect01').value;
    if (mode === "1") {
        document.getElementById('input_number').style.display = "block";
        document.getElementById('label_number').style.display = "block";
        document.getElementById('input_name').style.display = "none";
        document.getElementById('label_name').style.display = "none";
        document.getElementById('inputGroupSelect02').style.display = "none";
        document.getElementById('label_inputGroupSelect02').style.display = "none";
        document.getElementById('input_race_monster').style.display = "none";
        document.getElementById('label_race_monster').style.display = "none";
        document.getElementById('input_monster').style.display = "none";
        document.getElementById('label_monster').style.display = "none";
        document.getElementById('input_level').style.display = "none";
        document.getElementById('label_level').style.display = "none";
        document.getElementById('input_race_spell').style.display = "none";
        document.getElementById('label_race_spell').style.display = "none";
        document.getElementById('input_race_trap').style.display = "none";
        document.getElementById('label_race_trap').style.display = "none";
    }
    if (mode === "2") {
        document.getElementById('input_name').style.display = "block";
        document.getElementById('label_name').style.display = "block";
        document.getElementById('input_number').style.display = "none";
        document.getElementById('label_number').style.display = "none";
        document.getElementById('inputGroupSelect02').style.display = "none";
        document.getElementById('label_inputGroupSelect02').style.display = "none";
        document.getElementById('input_race_monster').style.display = "none";
        document.getElementById('label_race_monster').style.display = "none";
        document.getElementById('input_monster').style.display = "none";
        document.getElementById('label_monster').style.display = "none";
        document.getElementById('input_level').style.display = "none";
        document.getElementById('label_level').style.display = "none";
        document.getElementById('input_race_spell').style.display = "none";
        document.getElementById('label_race_spell').style.display = "none";
        document.getElementById('input_race_trap').style.display = "none";
        document.getElementById('label_race_trap').style.display = "none";
    }
    if (mode === "3") {
        document.getElementById('inputGroupSelect02').style.display = "block";
        document.getElementById('label_inputGroupSelect02').style.display = "block";
        document.getElementById('input_number').style.display = "none";
        document.getElementById('label_number').style.display = "none";
        document.getElementById('input_name').style.display = "none";
        document.getElementById('label_name').style.display = "none";
    }
}
function ChangeMonsterSpellTrap() {
    let monster_spell_trap = document.getElementById('inputGroupSelect02').value;
    if (monster_spell_trap === "monster_selected") {
        document.getElementById('input_race_monster').style.display = "block";
        document.getElementById('label_race_monster').style.display = "block";
        document.getElementById('input_monster').style.display = "block";
        document.getElementById('label_monster').style.display = "block";
        document.getElementById('input_level').style.display = "block";
        document.getElementById('label_level').style.display = "block";
        document.getElementById('input_race_spell').style.display = "none";
        document.getElementById('label_race_spell').style.display = "none";
        document.getElementById('input_race_trap').style.display = "none";
        document.getElementById('label_race_trap').style.display = "none";
    }
    if (monster_spell_trap === "spell_selected") {
        document.getElementById('input_race_spell').style.display = "block";
        document.getElementById('label_race_spell').style.display = "block";
        document.getElementById('input_race_monster').style.display = "none";
        document.getElementById('label_race_monster').style.display = "none";
        document.getElementById('input_race_trap').style.display = "none";
        document.getElementById('label_race_trap').style.display = "none";
        document.getElementById('input_monster').style.display = "none";
        document.getElementById('label_monster').style.display = "none";
        document.getElementById('input_level').style.display = "none";
        document.getElementById('label_level').style.display = "none";
    }
    if (monster_spell_trap === "trap_selected") {
        document.getElementById('input_race_trap').style.display = "block";
        document.getElementById('label_race_trap').style.display = "block";
        document.getElementById('input_race_spell').style.display = "none";
        document.getElementById('label_race_spell').style.display = "none";
        document.getElementById('input_race_monster').style.display = "none";
        document.getElementById('label_race_monster').style.display = "none";
        document.getElementById('input_monster').style.display = "none";
        document.getElementById('label_monster').style.display = "none";
        document.getElementById('input_level').style.display = "none";
        document.getElementById('label_level').style.display = "none";
    }
}
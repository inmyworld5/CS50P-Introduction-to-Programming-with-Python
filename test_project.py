from project import generate, check, check_length, check_special, check_a_z, check_num


def test_generate():
    password = generate(8)
    assert len(password) == 8
    password = generate(10)
    assert len(password) == 10


def test_check():
    assert check("tyIO89£#") == "Your password is just fine :)"
    assert (
        check("dsfghjjhgfdaf")
        == "❗Your password doesn't contain special characters\n❗Your password doesn't contain A-Z letters\n❗Your password doesn't contain numbers\n"
    )
    assert check("Adfg789fdf") == "❗Your password doesn't contain special characters\n"
    assert (
        check("sgsdf")
        == "❗Your password is too short\n❗Your password doesn't contain special characters\n❗Your password doesn't contain A-Z letters\n❗Your password doesn't contain numbers\n"
    )
    assert check("456sdf##") == "❗Your password doesn't contain A-Z letters\n"
    assert check("#7aGy") == "❗Your password is too short\n"
    assert check("sdfd##SDy") == "❗Your password doesn't contain numbers\n"


def test_check_length():
    assert check_length("7sd") == "❗Your password is too short"
    assert check_length("s7br9cfs") == None
    assert check_length("789gfghjh$%D") == None


def test_check_special():
    assert check_special("%78#sdT") == None
    assert (
        check_special("ASfgh89io")
        == "❗Your password doesn't contain special characters"
    )


def test_check_a_z():
    assert check_a_z("dfg7993£") == "❗Your password doesn't contain A-Z letters"
    assert check_a_z("ASfghj78") == None


def test_check_num():
    assert check_num("sdf4567") == None
    assert check_num("#fghFGtys.") == "❗Your password doesn't contain numbers"

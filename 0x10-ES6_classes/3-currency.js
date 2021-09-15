// Implement a class named Currency
class Currency {
    constructor(code, name) {
	if (typeOf (code) !== 'string') {
	    throw typeError('Code must be a string');
	} else if (typeOf (name) !== 'string')	{
            throw typeError('Name must be a string');
	} else {
	    this._name = name;
	    this._code = code;
	}
    }

    get name() {
	return this._name;
    }
    set name(newName) {
	if (typeOf (newName) !== 'string')  {
            throw typeError('Name must be a string');
        } else {
            this._name = newName;
	}
    }

    get code() {
	return this._code;
    }
    set code(newCode) {
	if (typeOf (newCode) !== 'string')  {
            throw typeError('Code must be a string');
        } else {
	    this._code = newCode;
	}
    }

    displayFullCurrency() {
	return `${this._name} (${this._code})`;
    }
}

export default Currency;

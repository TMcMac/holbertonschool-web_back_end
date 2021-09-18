// Do something with Currancy
import Currency from './3-currency';

class Pricing {
  constructor(amount, currancy) {
    this._amount = amount;
    this._currancy = currancy;
  }

  get amount() { return this._amount; }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') { throw TypeError('Amount must be a number'); }
    this._amount = newAmount;
  }

  get currency() { return this._currency; }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) { throw TypeError('Currency must be an instance of Currency'); }
    this._currency = newCurrency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw TypeError('Amount / Conversion Rate must be numbers');
    }
    return amount * conversionRate;
  }
}

export default Pricing;

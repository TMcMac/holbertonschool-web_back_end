// Extends class building
import Building from './5-building.js'

export default class SkyHighBuilding extends Building {
  consructor(sqft, floors) {
	  super(sqft);
	  this._floors = floors;
  }

  get sqft() {return this._sqft}
  get floors() {return this.floors}

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
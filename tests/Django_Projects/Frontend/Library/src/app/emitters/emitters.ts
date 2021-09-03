import {EventEmitter} from '@angular/core';

export class Emitters {
  static authEmitter = new EventEmitter<boolean>();
  static id = new EventEmitter<number>();
  static status = new EventEmitter<boolean>();
  static is_superuser = new EventEmitter<boolean>();
}
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddstaffbooksComponent } from './addstaffbooks.component';

describe('AddstaffbooksComponent', () => {
  let component: AddstaffbooksComponent;
  let fixture: ComponentFixture<AddstaffbooksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddstaffbooksComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddstaffbooksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

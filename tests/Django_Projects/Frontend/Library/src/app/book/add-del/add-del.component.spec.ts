import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddDelComponent } from './add-del.component';

describe('AddDelComponent', () => {
  let component: AddDelComponent;
  let fixture: ComponentFixture<AddDelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddDelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddDelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

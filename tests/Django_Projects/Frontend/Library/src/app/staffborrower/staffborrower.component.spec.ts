import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StaffborrowerComponent } from './staffborrower.component';

describe('StaffborrowerComponent', () => {
  let component: StaffborrowerComponent;
  let fixture: ComponentFixture<StaffborrowerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StaffborrowerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StaffborrowerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BannegstrComponent } from './bannegstr.component';

describe('BannegstrComponent', () => {
  let component: BannegstrComponent;
  let fixture: ComponentFixture<BannegstrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BannegstrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BannegstrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

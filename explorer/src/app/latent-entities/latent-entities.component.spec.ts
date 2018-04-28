import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LatentEntitiesComponent } from './latent-entities.component';

describe('LatentEntitiesComponent', () => {
  let component: LatentEntitiesComponent;
  let fixture: ComponentFixture<LatentEntitiesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LatentEntitiesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LatentEntitiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

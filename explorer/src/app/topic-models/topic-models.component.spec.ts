import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopicModelsComponent } from './topic-models.component';

describe('TopicModelsComponent', () => {
  let component: TopicModelsComponent;
  let fixture: ComponentFixture<TopicModelsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopicModelsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopicModelsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

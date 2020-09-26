import { NgModule } from '@angular/core';

import { MiappSharedLibsModule, JhiAlertComponent, JhiAlertErrorComponent } from './';

@NgModule({
  imports: [MiappSharedLibsModule],
  declarations: [JhiAlertComponent, JhiAlertErrorComponent],
  exports: [MiappSharedLibsModule, JhiAlertComponent, JhiAlertErrorComponent]
})
export class MiappSharedCommonModule {}

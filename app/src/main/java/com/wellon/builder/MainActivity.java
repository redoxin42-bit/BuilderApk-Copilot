package com.wellon.builder;
import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;
import android.graphics.Color;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        tv.setText("Wellon AI Builder\n> Status: Online\n> System: Ready to hack...");
        tv.setBackgroundColor(Color.BLACK);
        tv.setTextColor(Color.GREEN);
        tv.setPadding(30, 30, 30, 30);
        setContentView(tv);
    }
}
